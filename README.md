# SCOPE
# Data
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
  - `UR90`: Path to the UniRef90 sequence database
**Note:** 
The UniRef90 database should be preprocessed using `makeblastdb` prior to use.
