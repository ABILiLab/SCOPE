# SCOPE reproducibility and Colab demonstration

This directory provides a CPU environment specification, a configurable
SCOPE pipeline, a model checkpoint, and a Google Colab demonstration
using prepared features.

## Files

- `environment_cpu.yml`: Python 3.10 CPU environment with tested
  dependency versions, without machine-specific paths or build identifiers.
- `scope_reproduction_candidate_20261028.tar.gz`: versioned source
  archive containing the configurable feature-generation and prediction
  entry points.
- `best.pth`: SCOPE checkpoint used in the reproducibility demonstration.
- `1smn_A_prepared_features.zip`: prepared features for the 245-residue
  example protein 1smn-A.
- `SCOPE_Colab_demo.ipynb`: CPU inference notebook for Google Colab.

## Google Colab: inference from prepared features

[Open in Colab](https://colab.research.google.com/github/ABILiLab/SCOPE/blob/main/reproducibility/SCOPE_Colab_demo.ipynb)

1. Download the source archive, `best.pth`, and
   `1smn_A_prepared_features.zip` from this directory.
2. Open the notebook in Colab and connect to a CPU runtime.
3. Run the environment-installation cell.
4. Upload the source archive and `best.pth` when prompted.
5. Upload `1smn_A_prepared_features.zip` when prompted.
6. Run the prediction cell and download the results archive.

The notebook installs an isolated Python 3.10 environment. A GPU is not
required for this demonstration.

This demonstration starts from prepared features. It does not run
PSI-BLAST, HHblits, or ProtT5 feature extraction in Colab. Uploading only
a FASTA or PDB file is therefore insufficient for this notebook.

The downloaded results include residue-level predictions, a completion
record, a run log, and a manifest recording input hashes and the command
used.

## Linux CPU workflow

Create and activate the environment:

    conda env create -f environment_cpu.yml
    conda activate scope-reproduction-cpu
    python -m pip check

Extract the source archive:

    tar -xzf scope_reproduction_candidate_20261028.tar.gz

Edit `scope_reproduction_candidate/config.example.json` to specify
the input FASTA, matching PDB structure, SCOPE checkpoint, ProtT5
directory, external executables, and database prefixes.

Run the pipeline using a new output directory:

    python scope_reproduction_candidate/scope_raw_pipeline.py \
        --config /absolute/path/config.json \
        --output /absolute/path/new_output

The validated adapter accepts one protein of 2–1000 residues and a
matching PDB chain with sequence-based residue numbering. Mapped
residues must match the sequence and must not contain insertion codes.
Arbitrary PDB residue numbering is not supported by this adapter.

## External resources for feature generation

The full Linux workflow additionally requires:

- PSI-BLAST and the sequence database specified in the configuration;
- HHblits and a compatible HH-suite database;
- the complete ProtT5 model directory;
- a matching protein structure and the SCOPE checkpoint.

These external databases and the ProtT5 model are not included in this
directory. Record the database release and tool versions used, because
changing these resources can change the generated features.

Resource links:

- BLAST: https://blast.ncbi.nlm.nih.gov/doc/blast-help/downloadblastdata.html
- HH-suite: https://github.com/soedinglab/hh-suite
- ProtT5: https://huggingface.co/Rostlab/prot_t5_xl_uniref50

## Validation and scope

The packaged Linux workflow was tested in an independently installed
Python 3.10 CPU environment. It generated features and predictions for
the 245 residues of 1smn-A, reproducing the archived CPU reference output.
