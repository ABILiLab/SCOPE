# SCOPE: Gaussian-regularized graph learning for enzyme catalytic residue prediction
Accurate identification of catalytic residues is central to understanding enzyme mechanisms and engineering biocatalysts, yet annotation remains challenging because experimentally validated sites are sparse. Here, we present SCOPE, a graph learning framework for catalytic residue prediction that integrates evolutionary, physicochemical, and three-dimensional structural information at the residue level. SCOPE represents enzymes as residue-level structural graphs and incorporates a Gaussian auxiliary training objective that aggregates structure-aware representations along sequence order. Evaluations across five benchmark datasets, CATH family-disjoint retraining and the external CataloDB benchmark assess predictive performance and generalization. Structural analyses associate complete catalytic-residue recovery with compact active-site arrangements. We further validated SCOPE prospectively across four enzymes using site-directed mutagenesis and activity assays, confirming multiple predicted residues as functionally important. These results support SCOPE as a framework for catalytic residue annotation and prioritizing functional sites for experimental investigation.
# Data
Download the dataset from Hugging Face: <https://huggingface.co/datasets/Biocollab/SCREEN/tree/main>. Extract the downloaded files into the `Dataset` directory.
# Installation
## Environment
Navigate to the `SCOPE` directory and create the environment using: 
```python
conda env create -f environment.yml
```
Then activate the environment:
```python
conda activate scope
```
## Tool description
### BLAST+ for PSSM Profile Generation
#### Download and Installation
BLAST+ is available from the NCBI FTP server: <https://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/>
#### Documentation
For detailed instructions, please refer to the official NCBI guide: <https://www.ncbi.nlm.nih.gov/books/NBK52640/>
#### Configuration
Before running feature extraction, ensure that the following paths are correctly specified in `feature_extract.py`:
  - `PSIBLAST`: Path to the PSI-BLAST executable
  - `UR90`: Path to the UniRef90 sequence database (The UniRef90 database should be preprocessed using `makeblastdb` prior to use)
### HH-suite for HHM Profile Generation
#### Installation
HH-suite can be installed by following the official instructions: <https://github.com/soedinglab/hh-suite>
#### Database Download
Download the prebuilt UniClust30 database (version 2018_08): <http://wwwuser.gwdg.de/~compbiol/uniclust/2018_08/uniclust30_2018_08_hhsuite.tar.gz>
#### Configuration
Before running feature extraction, configure the following paths in `feature_extract.py`:
  - `HHBLITS`: Path to the HHblits executable
  - `HHDB`: Path to the UniClust30 database (Make sure the UniClust30 database is fully downloaded and properly extracted before use)
### ProtT5 Weights for Evolutionary Embedding
In `evofea_embedding.py`, set the model directory as specified in the comments:
  - MODEL_DIR: Path to the ProtT5 pretrained model weights
Ensure that all required model files are correctly downloaded and placed in the specified directory before running the embedding script.
# Feature Extraction
Navigate to the `SCOPE` directory and run:
```python
python feature_extract.py
```
This step will generate and/or update intermediate feature files, including PSSM profiles, HHM profiles, DSSP structural features, atomic features, contact maps, and sequence-based features; ensure that all required external tools (e.g., BLAST+, HH-suite, DSSP) are properly installed and configured before running it.
# Model Training
(Optional) Set the `LOG_PATH` in `train_deepgcn_with_gaussion_weight.py` as specified in the comments. Start training by running:
```python
python train_deepgcn_with_gaussion_weight.py
```
# Residue Scoring with the SCOPE Model
Run inference using the provided example input (`Example`):
```python
python infer.py
```
The results will be saved to the `InferResult` directory by default.
# GUI (Graphical user interface)
## Introduction
The platform integrates the SCOPE model for enzyme catalytic site prediction. It allows users to upload enzyme PDB structures or FASTA sequences to identify potential catalytic residues and visualize residue-level prediction scores.
## Running Methods
Launch the graphical user interface (GUI) by running:
```python
python SCOPE_GUI_infer.py
```
## Use SCOPE in this platform
After successfully running the `SCOPE_GUI_infer.py` file, you can follow the steps below to use SCOPE on our platform.
### Input Data
- Please upload a PDB file and a FASTA sequence for the enzyme you want to predict!
![image](GUI_img/Input-data.png)
### Online feature extraction
- Please perform online feature extraction by clicking `Yes` to start; if the corresponding features are already cached, this step will be skipped.
![image](GUI_img/feature-extraction.png)
### Predict and save results
- Click the `Predict` button to perform the prediction operation.
![image](GUI_img/pre-result.png)
- If you want to continue to predict other proteins, please click `Clean` button first.
### Results display
#### Prediction Table
- The prediction results are presented in a table containing the residue position, amino acid type, prediction score, and predicted label.
![image](GUI_img/GUI-table-result.png)
#### 3D Structure View
- Predicted catalytic residues are highlighted in the interactive 3D structure to show their spatial locations and surrounding environment.
![image](GUI_img/GUI-3D-result.png)
#### Sequence View
- The sequence panel displays residue-level prediction scores and labels, enabling intuitive interpretation along the protein sequence.
![image](GUI_img/GUI-seq-result.png)
