# SCOPE
# Data
Download the dataset from Hugging Face: <https://huggingface.co/datasets/Biocollab/SCREEN/tree/main>. Extract the downloaded files into the `Dataset` directory.
# Installation
## Environment

## Feature extraction and tool description
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

