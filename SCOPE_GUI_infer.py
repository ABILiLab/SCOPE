import os
import pickle
import argparse
import sys
import hashlib
from typing import Callable, Dict, List, Optional

import h5py
import numpy as np
import pandas as pd
import torch
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader

from scope_model_utils import (
    SCOPE,
    INPUT_DIM,
    HIDDEN_DIM,
    NLAYER,
    DROPOUT,
    NUM_CLASSES,
    BATCH_SIZE,
    embedding,
    get_atom_features,
    load_graph,
)


SCOPE_GUI_DIR = os.path.abspath(os.path.dirname(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCOPE_GUI_DIR, ".."))
DATA_DIR = os.path.join(SCOPE_GUI_DIR, "SCOPE_data")
# NOTE: feature_extract.py 里大量使用字符串拼接（如 data_dir + "fasta/..."）
# 依赖 data_dir 末尾带路径分隔符，因此这里强制加上 os.sep，避免出现
# ".../SCOPE_datafasta/..." 这种路径错误。
DATA_DIR = DATA_DIR + os.sep
CHECKPOINT_PATH = os.path.join(SCOPE_GUI_DIR, "checkpoints", "best.pth")


def _read_fasta_sequence(fasta_path: str) -> str:
    with open(fasta_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    # assume format: >id \n SEQ
    for line in lines:
        if not line.startswith(">"):
            return line.replace(" ", "").replace("\t", "")
    raise ValueError(f"No sequence found in fasta: {fasta_path}")


def _normalize_protein_id(raw_id: str) -> str:
    """
    SCOPE pipeline expects IDs like: <pdb_id>-<chain>
    Examples: 1chu-A / 1chu_A (will be normalized) / 1gkm-_ (chain '_' -> keep, later treated as 'A')
    """
    raw_id = raw_id.strip()
    if "-" in raw_id:
        return raw_id
    if "_" in raw_id:
        parts = raw_id.split("_")
        if len(parts) < 2:
            return raw_id
        # replace only the first underscore
        return parts[0] + "-" + parts[1]
    raise ValueError(
        f"Protein id must look like '<pdb_id>-<chain>' (e.g. '1chu-A'), got: {raw_id}"
    )


def _parse_fasta_multi(fasta_path: str) -> Dict[str, str]:
    """
    Parse multi-FASTA.
    Header must contain protein id in first token, e.g.:
      >1chu-A
      MKT...
    """
    if not os.path.exists(fasta_path):
        raise FileNotFoundError(f"Missing fasta: {fasta_path}")

    prot2seq: Dict[str, str] = {}
    current_id = None  # type: str | None
    seq_chunks: List[str] = []

    with open(fasta_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_id is not None:
                    prot2seq[current_id] = "".join(seq_chunks).strip()
                raw_id = line[1:].split()[0]
                current_id = _normalize_protein_id(raw_id)
                seq_chunks = []
            else:
                seq_chunks.append(line.replace(" ", "").replace("\t", "").upper())

    if current_id is not None:
        prot2seq[current_id] = "".join(seq_chunks).strip()

    if not prot2seq:
        raise ValueError(f"No sequences parsed from fasta: {fasta_path}")
    return prot2seq


def load_fasta_sequences(fasta_path: str) -> Dict[str, str]:

    return _parse_fasta_multi(fasta_path)


def _extract_chain_pdb(in_pdb_path: str, out_pdb_path: str, chain_id: str) -> None:
    """
    Create a single-chain PDB for downstream steps.
    Chain selection uses PDB column 22 (index 21), consistent with feature_extract.py.
    """
    if not os.path.exists(in_pdb_path):
        raise FileNotFoundError(f"Missing pdb: {in_pdb_path}")

    kept_lines: List[str] = []
    ter_found = False

    with open(in_pdb_path, "r") as f:
        for line in f:
            if line.startswith("ATOM") and len(line) > 21 and line[21] == chain_id:
                kept_lines.append(line)
            elif line.startswith("TER") and len(line) > 21 and line[21] == chain_id:
                kept_lines.append(line)
                ter_found = True
                break

    if not kept_lines:
        raise RuntimeError(
            f"Chain '{chain_id}' not found in pdb: {in_pdb_path}. "
            f"Check that your PDB matches the id '{out_pdb_path}'."
        )

    # Ensure TER/END exist
    if not ter_found:
        kept_lines.append("TER\n")
    kept_lines.append("END\n")

    os.makedirs(os.path.dirname(out_pdb_path), exist_ok=True)
    with open(out_pdb_path, "w") as out:
        out.writelines(kept_lines)


def _hash_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _source_pdb_hash_path(prot: str) -> str:
    return os.path.join(DATA_DIR, "cache_manifest", f"{prot}.source_pdb.sha256")


def _write_source_pdb_hash(prot: str, user_pdb_path: str) -> None:
    d = os.path.join(DATA_DIR, "cache_manifest")
    os.makedirs(d, exist_ok=True)
    with open(_source_pdb_hash_path(prot), "w") as f:
        f.write(_hash_file(user_pdb_path))


def _cache_valid_for_protein(prot: str, user_pdb_path: str) -> bool:
    """
    Reuse disk cache only when feature files exist and (if manifest exists)
    the SHA256 of the user-provided PDB matches the last successful extraction.
    """
    if not _protein_features_exist(prot):
        return False
    hpath = _source_pdb_hash_path(prot)
    if not os.path.exists(hpath):
        return True
    with open(hpath, "r") as f:
        old = f.read().strip()
    return old == _hash_file(user_pdb_path)


def _prepare_inputs_from_user(
    fasta_path: str, pdb_path: str, protein_list: List[str], prot_seq: Dict[str, str]
) -> Dict[str, str]:
    """
    Copy/write user inputs into SCOPE_data layout:
    - SCOPE_data/fasta/<prot>.fa
    - SCOPE_data/PDB/SavechainPDB/<prot>.pdb
    Returns mapping protein_id -> absolute path of the user PDB file used as source (for cache fingerprint).
    """
    fasta_dir = os.path.join(DATA_DIR, "fasta")
    savechain_dir = os.path.join(DATA_DIR, "PDB", "SavechainPDB")
    os.makedirs(fasta_dir, exist_ok=True)
    os.makedirs(savechain_dir, exist_ok=True)
    prot_to_user_pdb: Dict[str, str] = {}

    # Write per-protein fasta files (feature_extract expects fasta/<prot>.fa)
    for prot in protein_list:
        seq = prot_seq[prot]
        fasta_file = os.path.join(fasta_dir, f"{prot}.fa")
        with open(fasta_file, "w") as f:
            f.write(f">{prot}\n{seq}\n")

    # Prepare per-protein single-chain PDBs
    if os.path.isdir(pdb_path):
        for prot in protein_list:
            pdb_candidates = [
                os.path.join(pdb_path, f"{prot}.pdb"),
                os.path.join(pdb_path, f"{prot.replace('-', '_')}.pdb"),
            ]
            in_pdb = next((p for p in pdb_candidates if os.path.exists(p)), None)
            if in_pdb is None:
                raise FileNotFoundError(
                    f"Cannot find pdb for '{prot}'. Looked for: {pdb_candidates}"
                )
            prot_to_user_pdb[prot] = os.path.abspath(in_pdb)
            chain_id = prot.split("-", 1)[1]
            if chain_id == "_":
                chain_id = "A"
            out_pdb = os.path.join(savechain_dir, f"{prot}.pdb")
            _extract_chain_pdb(in_pdb, out_pdb, chain_id)
    else:
        # single pdb file
        if len(protein_list) != 1:
            raise ValueError(
                "When --pdb is a file, --fasta must contain exactly one protein entry."
            )
        prot = protein_list[0]
        prot_to_user_pdb[prot] = os.path.abspath(pdb_path)
        chain_id = prot.split("-", 1)[1]
        if chain_id == "_":
            chain_id = "A"
        out_pdb = os.path.join(savechain_dir, f"{prot}.pdb")
        _extract_chain_pdb(pdb_path, out_pdb, chain_id)
    return prot_to_user_pdb


def check_scope_features_ready(fasta_path: str, pdb_path: str):
    """

    Returns:
        (ok: bool, protein_list: List[str], error_message: str)
    """
    try:
        _ensure_dirs()
        prot_seq = _parse_fasta_multi(fasta_path)
        protein_list = list(prot_seq.keys())
        prot_to_user_pdb = _prepare_inputs_from_user(fasta_path, pdb_path, protein_list, prot_seq)
        for p in protein_list:
            if not _cache_valid_for_protein(p, prot_to_user_pdb[p]):
                return (
                    False,
                    protein_list,
                    f"Protein \"{p}\" is missing features or the current PDB does not match cached features. "
                    f"Run Extract features above first.",
                )
        return True, protein_list, ""
    except Exception as e:
        return False, [], str(e)


def _ensure_dirs():
    # These dirs are referenced by feature_extract and by prediction code.
    required = [
        os.path.join(DATA_DIR, "fasta"),
        os.path.join(DATA_DIR, "PDB", "SavechainPDB"),
        os.path.join(DATA_DIR, "pssm"),
        os.path.join(DATA_DIR, "hhm"),
        os.path.join(DATA_DIR, "dssp"),
        os.path.join(DATA_DIR, "Atom_feas"),
        os.path.join(DATA_DIR, "seqfea"),
        os.path.join(DATA_DIR, "contact_map"),
        os.path.join(DATA_DIR, "Prot5"),
    ]
    for d in required:
        os.makedirs(d, exist_ok=True)


def _resolve_all_assign_dir() -> str:
    """
    feature_extract.seq_fea_generate reads './Dataset/all_assign.txt' as a relative path.
    We ensure cwd is set to a directory that contains Dataset/all_assign.txt.
    """
    # NOTE:
    # Keep this list aligned with your repo layout.
    # Please modify only these candidate directories if needed.
    candidates = [
        os.path.join(REPO_ROOT, "0828"),
        os.path.join(REPO_ROOT, "SCOPE_plus"),
    ]
    for c in candidates:
        if os.path.exists(os.path.join(c, "Dataset", "all_assign.txt")):
            return c
    raise FileNotFoundError("Cannot find Dataset/all_assign.txt in repo candidates.")


def _ensure_biotoolbox_on_path() -> None:
    """
    `SCOPE_GUI/feature_extract.py` depends on `biotoolbox`.
    The repository contains `biotoolbox` under e.g. `SCOPE_main/biotoolbox`.
    When running from `SCOPE_GUI`, Python may not have that directory on sys.path.
    """
    # NOTE:
    # Keep this list aligned with your repo layout.
    # Please modify only these candidate directories if needed.
    candidates = [
        os.path.join(REPO_ROOT, "SCOPE_main"),
        os.path.join(REPO_ROOT, "0828"),
        os.path.join(REPO_ROOT, "SCOPE_plus", "Feature_extracter"),
    ]
    for c in candidates:
        if os.path.exists(os.path.join(c, "biotoolbox")) and c not in sys.path:
            sys.path.insert(0, c)


def _read_pdb_ids() -> List[str]:
    pdb_ids_path = os.path.join(DATA_DIR, "pdb_ids.txt")
    if not os.path.exists(pdb_ids_path):
        raise FileNotFoundError(f"Missing pdb_ids.txt: {pdb_ids_path}")
    with open(pdb_ids_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def _pdbid_to_savechain_pdb(prot: str) -> str:
    return os.path.join(DATA_DIR, "PDB", "SavechainPDB", f"{prot}.pdb")


def _ensure_savechain_pdb(feature_extract, protein_list: List[str]):
    """
    Ensure SavechainPDB/<prot>.pdb exists for each prot.
    If missing, try to download PDB.gz and then save chain PDB.
    """
    missing = [p for p in protein_list if not os.path.exists(_pdbid_to_savechain_pdb(p))]
    if not missing:
        return

    # download_pdb expects data_path like ".../PDB/"
    feature_extract.download_pdb(protein_list, os.path.join(DATA_DIR, "PDB") + "/")
    feature_extract.SaveChainPDB(protein_list, os.path.join(DATA_DIR, "PDB") + "/")


def _ensure_fasta_and_sequences(feature_extract, protein_list: List[str]) -> Dict[str, str]:
    """
    Prediction uses fasta/<prot>.fa to get the raw sequence.
    If fasta is missing, derive sequence from generated Atom_feas/<prot>.csv.pkl (get_pdb_DF).
    """
    prot_seq: Dict[str, str] = {}
    fasta_dir = os.path.join(DATA_DIR, "fasta")
    for prot in protein_list:
        fasta_path = os.path.join(fasta_dir, f"{prot}.fa")
        if os.path.exists(fasta_path):
            prot_seq[prot] = _read_fasta_sequence(fasta_path)
            continue

        # Derive from PDB chain -> get_pdb_DF -> Atom_feas/<prot>.csv.pkl['sequence']
        feature_extract.get_pdb_DF(prot, data_path=DATA_DIR)
        csv_pkl = os.path.join(DATA_DIR, "Atom_feas", f"{prot}.csv.pkl")
        with open(csv_pkl, "rb") as f:
            tmp = pickle.load(f)
        prot_seq[prot] = tmp["sequence"]

        # Write per-protein fasta for psiblast/hhblits and for inference reading.
        with open(fasta_path, "w") as out:
            out.write(f">{prot}\n{prot_seq[prot]}\n")

    return prot_seq


def _protein_features_exist(prot: str) -> bool:
    def exists(path: str) -> bool:
        return os.path.exists(path)

    required_files = [
        os.path.join(DATA_DIR, "contact_map", f"{prot}.npy"),
        os.path.join(DATA_DIR, "pssm", "processed_pssm", f"{prot}.npy"),
        os.path.join(DATA_DIR, "hhm", "processed_hhm", f"{prot}.npy"),
        os.path.join(DATA_DIR, "dssp", "matched_dssp", f"{prot}.npy"),
        os.path.join(DATA_DIR, "Atom_feas", "matched_atomfea", f"{prot}.npy"),
        os.path.join(DATA_DIR, "seqfea", f"{prot}.npy"),
    ]
    if not all(exists(p) for p in required_files):
        return False

    h5_path = os.path.join(DATA_DIR, "Prot5", "train_per_residue_embeddings.h5")
    if not os.path.exists(h5_path):
        return False
    try:
        with h5py.File(h5_path, "r") as f:
            return prot in f.keys()
    except OSError:
        return False


def extract_features_and_cache_from_fasta_pdb(
    fasta_path: str,
    pdb_path: str,
    status_callback: Optional[Callable[[str], None]] = None,
) -> List[str]:
    """
    Step 1 (user mode):
    - Parse multi-FASTA: headers define protein ids (<pdb_id>-<chain>)
    - Copy/extract PDB chain into: SCOPE_data/PDB/SavechainPDB/<prot>.pdb
    - Write fasta into: SCOPE_data/fasta/<prot>.fa and fasta/allseq.fa
    - Run feature_extract to generate missing cached features under SCOPE_data
    - Return protein_list
    """
    def _notify(msg: str) -> None:
        print(msg)
        if status_callback is not None:
            status_callback(msg)

    _ensure_dirs()
    prot_seq = _parse_fasta_multi(fasta_path)
    protein_list = list(prot_seq.keys())

    # Import lazily because it pulls heavy deps and external feature tools.
    _ensure_biotoolbox_on_path()
    # Ensure local `SCOPE_GUI/feature_extract.py` is picked up instead of other
    # similarly-named modules elsewhere in the repo.
    if SCOPE_GUI_DIR in sys.path:
        sys.path.remove(SCOPE_GUI_DIR)
    sys.path.insert(0, SCOPE_GUI_DIR)
    import feature_extract as feature_extract

    prot_to_user_pdb = _prepare_inputs_from_user(fasta_path, pdb_path, protein_list, prot_seq)

    # Ensure fasta/allseq.fa exists for evo_embedding
    feature_extract.write_all_fasta(DATA_DIR, protein_list, prot_seq)

    missing = [
        p for p in protein_list if not _cache_valid_for_protein(p, prot_to_user_pdb[p])
    ]
    if not missing:
        _notify("[SCOPE_GUI_infer] Local features are up to date for this PDB; skipping feature extraction.")
        for p in protein_list:
            _write_source_pdb_hash(p, prot_to_user_pdb[p])
        return protein_list

    _notify(
        f"[SCOPE_GUI_infer] Extracting features for {len(missing)}/{len(protein_list)} protein(s); this may take a long time…"
    )

    # 1) Contact maps
    _notify("[SCOPE_GUI_infer] Step 1/4: contact maps …")
    for prot in missing:
        feature_extract.write_contact_map(prot, prot2seq=prot_seq, data_path=DATA_DIR)

    # 2) PSSM / HMM / DSSP + matched DSSP
    _notify("[SCOPE_GUI_infer] Step 2/4: PSSM / HHM / DSSP (often the slowest) …")
    for prot in missing:
        feature_extract.Multi_process_PSSM_generation(prot, data_path=DATA_DIR)
    feature_extract.cal_PSSM(missing, os.path.join(DATA_DIR, "pssm") + "/")
    feature_extract.cal_HMM(missing, os.path.join(DATA_DIR, "hhm") + "/")
    feature_extract.cal_DSSP(missing, os.path.join(DATA_DIR, "dssp") + "/")
    for prot in missing:
        feature_extract.matched_dssp(
            prot,
            prot_seq[prot],
            os.path.join(DATA_DIR, "PDB", "SavechainPDB") + "/",
            os.path.join(DATA_DIR, "dssp") + "/",
        )

    # 3) Atom features / seq features
    _notify("[SCOPE_GUI_infer] Step 3/4: atom and sequence features …")
    for prot in missing:
        feature_extract.get_pdb_DF(prot, data_path=DATA_DIR)
    feature_extract.cal_atomFea(missing, DATA_DIR)

    # seq_fea_generate depends on Dataset/all_assign.txt relative path.
    all_assign_dir = _resolve_all_assign_dir()
    old_cwd = os.getcwd()
    try:
        os.chdir(all_assign_dir)
        for prot in missing:
            feature_extract.matched_atomfea(prot, prot_seq[prot], DATA_DIR)
            feature_extract.seq_fea_generate(prot, prot_seq[prot], DATA_DIR)
    finally:
        os.chdir(old_cwd)

    # 4) ProtT5 embeddings
    evo_embeddings_path = os.path.join(DATA_DIR, "Prot5", "train_per_residue_embeddings.h5")
    need_evo = False
    if not os.path.exists(evo_embeddings_path):
        need_evo = True
    else:
        with h5py.File(evo_embeddings_path, "r") as f:
            for prot in protein_list:
                if prot not in f.keys():
                    need_evo = True
                    break
    if need_evo:
        _notify("[SCOPE_GUI_infer] Step 4/4: ProtT5 embeddings (may be very slow) …")
        feature_extract.evo_embedding(DATA_DIR)

    # Final check
    still_missing = [p for p in protein_list if not _protein_features_exist(p)]
    if still_missing:
        raise RuntimeError(f"Feature extraction incomplete. Still missing: {still_missing}")

    for p in protein_list:
        _write_source_pdb_hash(p, prot_to_user_pdb[p])
    _notify("[SCOPE_GUI_infer] Feature extraction and caching finished.")
    return protein_list


def extract_features_and_cache():
    """
    Step 1: generate/cached all intermediate features under `SCOPE_GUI/SCOPE_data`,
    so `predict_results()` can run without needing to regenerate them.
    """
    _ensure_dirs()
    protein_list = _read_pdb_ids()

    # Import lazily because it pulls heavy deps and external feature tools.
    _ensure_biotoolbox_on_path()
    # Ensure local `SCOPE_GUI/feature_extract.py` is picked up instead of other
    # similarly-named modules elsewhere in the repo.
    if SCOPE_GUI_DIR in sys.path:
        sys.path.remove(SCOPE_GUI_DIR)
    sys.path.insert(0, SCOPE_GUI_DIR)
    import feature_extract as feature_extract

    # Ensure chain PDB exists before building contact maps etc.
    _ensure_savechain_pdb(feature_extract, protein_list)

    # Ensure fasta + sequences; feature_extract needs prot_seq for contact map + dssp alignment.
    prot_seq = _ensure_fasta_and_sequences(feature_extract, protein_list)

    # Ensure fasta/allseq.fa exists for evo_embedding
    feature_extract.write_all_fasta(DATA_DIR, protein_list, prot_seq)

    missing = [p for p in protein_list if not _protein_features_exist(p)]
    if not missing:
        print("[SCOPE_GUI_infer] Features already cached. Skip extraction.")
        return

    print(f"[SCOPE_GUI_infer] Missing features for {len(missing)}/{len(protein_list)} proteins. Extracting...")

    # 1) Contact maps
    for prot in missing:
        feature_extract.write_contact_map(prot, prot2seq=prot_seq, data_path=DATA_DIR)

    # 2) PSSM / HMM / DSSP + matched DSSP
    for prot in missing:
        feature_extract.Multi_process_PSSM_generation(prot, data_path=DATA_DIR)
    feature_extract.cal_PSSM(missing, os.path.join(DATA_DIR, "pssm") + "/")
    feature_extract.cal_HMM(missing, os.path.join(DATA_DIR, "hhm") + "/")
    feature_extract.cal_DSSP(missing, os.path.join(DATA_DIR, "dssp") + "/")
    for prot in missing:
        if prot in prot_seq:
            feature_extract.matched_dssp(
                prot,
                prot_seq[prot],
                os.path.join(DATA_DIR, "PDB", "SavechainPDB") + "/",
                os.path.join(DATA_DIR, "dssp") + "/",
            )

    # 3) Atom features / seq features
    # get_pdb_DF and cal_atomFea are mutually dependent; run only for missing set.
    for prot in missing:
        feature_extract.get_pdb_DF(prot, data_path=DATA_DIR)
    feature_extract.cal_atomFea(missing, DATA_DIR)

    # seq_fea_generate depends on Dataset/all_assign.txt relative path.
    all_assign_dir = _resolve_all_assign_dir()
    old_cwd = os.getcwd()
    try:
        os.chdir(all_assign_dir)
        for prot in missing:
            if prot in prot_seq:
                feature_extract.matched_atomfea(prot, prot_seq[prot], DATA_DIR)
                feature_extract.seq_fea_generate(prot, prot_seq[prot], DATA_DIR)
    finally:
        os.chdir(old_cwd)

    # 4) ProtT5 embeddings
    evo_embeddings_path = os.path.join(DATA_DIR, "Prot5", "train_per_residue_embeddings.h5")
    need_evo = False
    if not os.path.exists(evo_embeddings_path):
        need_evo = True
    else:
        with h5py.File(evo_embeddings_path, "r") as f:
            for prot in protein_list:
                if prot not in f.keys():
                    need_evo = True
                    break
    if need_evo:
        print("[SCOPE_GUI_infer] Generating ProtT5 embeddings (may take time)...")
        feature_extract.evo_embedding(DATA_DIR)

    # Final check
    still_missing = [p for p in protein_list if not _protein_features_exist(p)]
    if still_missing:
        raise RuntimeError(f"Feature extraction incomplete. Still missing: {still_missing}")

    print("[SCOPE_GUI_infer] Feature extraction + caching done.")


class _InferDataset(Dataset):
    def __init__(self, protein_list: List[str], data_dir: str):
        self.protein_list = protein_list
        self.data_dir = data_dir

    def __len__(self) -> int:
        return len(self.protein_list)

    def __getitem__(self, index: int):
        prot = self.protein_list[index]
        fasta_path = os.path.join(self.data_dir, "fasta", f"{prot}.fa")
        with open(fasta_path, "r") as f:
            sequence = f.read().split("\n")[1].strip()

        pssm_feature, hmm_feature, evo_feature = embedding(prot, self.data_dir)
        atom_features, seq_feature = get_atom_features(prot, self.data_dir)
        node_features = np.concatenate([pssm_feature, hmm_feature, atom_features, seq_feature], axis=1)
        graph = load_graph(prot, self.data_dir)

        return prot, sequence, node_features[:1000], graph[:1000, :1000], evo_feature[:1000]


def predict_results():
    """
    Step 2: load cached features from `SCOPE_GUI/SCOPE_data` and run inference.
    Outputs into `SCOPE_GUI/SCOPE_data/InferResult/`.
    """
    protein_list = _read_pdb_ids()
    predict_results_for_protein_list(protein_list)


def predict_results_for_protein_list(
    protein_list: List[str],
    status_callback: Optional[Callable[[str], None]] = None,
) -> None:
    """
    Step 2: run inference for a provided protein list.
    All inputs are read from `SCOPE_data`.
    """
    def _notify(msg: str) -> None:
        print(msg)
        if status_callback is not None:
            status_callback(msg)

    _notify("[SCOPE_GUI_infer] Loading features and running model inference …")
    dataset = _InferDataset(protein_list, DATA_DIR)
    loader = DataLoader(dataset=dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=0)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = SCOPE(NLAYER, INPUT_DIM, HIDDEN_DIM, NUM_CLASSES, DROPOUT)
    state = torch.load(CHECKPOINT_PATH, map_location="cpu")
    model.load_state_dict(state)
    model.to(device)
    model.eval()

    out_dir = os.path.join(DATA_DIR, "InferResult")
    os.makedirs(out_dir, exist_ok=True)

    softmax = torch.nn.Softmax(dim=1)

    with torch.no_grad():
        for batch in loader:
            prot_names, seqs, node_features, graphs, evo_feature = batch
            prot_names = list(prot_names)
            # node_features/graphs/evo_feature already have leading dim from batch_size
            node_features = node_features.squeeze(0).to(device)
            graphs = graphs.squeeze(0).to(device)
            evo_feature = evo_feature.squeeze(0).to(device)

            y_pred, _, _ = model(node_features, graphs, evo_feature)
            y_pred = softmax(y_pred / 8).detach().cpu().numpy()

            prot = prot_names[0]
            seq = seqs[0]
            with open(os.path.join(out_dir, prot), "w") as f:
                for i in range(y_pred.shape[0]):
                    f.write(seq[i] + "\t" + str(y_pred[i][1]) + "\n")

    _notify(f"[SCOPE_GUI_infer] Prediction done. Output: {out_dir}/<protein_id>")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fasta",
        type=str,
        default=None,
        help="Input multi-FASTA containing protein ids in headers (e.g. '>1chu-A').",
    )
    parser.add_argument(
        "--pdb",
        type=str,
        default=None,
        help="Input PDB file (single entry) or directory (named as <prot>.pdb).",
    )
    args = parser.parse_args()

    if args.fasta and args.pdb:
        protein_list = extract_features_and_cache_from_fasta_pdb(args.fasta, args.pdb)
        predict_results_for_protein_list(protein_list)
    elif args.fasta or args.pdb:
        raise SystemExit("Please provide both --fasta and --pdb (or provide neither for pdb_ids mode).")
    else:
        extract_features_and_cache()
        predict_results()

