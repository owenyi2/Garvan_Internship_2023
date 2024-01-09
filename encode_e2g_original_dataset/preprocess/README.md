Input file: 
- [EPCrisprBenchmark_ensemble_data_GRCh38.K562_ENCDO000AAD_ENCFF325RTP_DNaseOnly_features_NAfilled.tsv](https://raw.githubusercontent.com/karbalayghareh/ENCODE-E2G/main/data/crispri/EPCrisprBenchmark_ensemble_data_GRCh38.K562_ENCDO000AAD_ENCFF325RTP_DNaseOnly_features_NAfilled.tsv)

Process:
- `main.ipynb`: Downloads input file from GitHub first. Documents and runs preprocessing steps. See this for explanation of preprocessing steps. 
- `main.py`: Does same thing as above but in a shorter less documented python script. Except does not download input file. Please `wget` it first. Easier to run on terminal

Dependencies:
- `pandas`

Output file:
- EPCrisprBenchmark_ensemble_data_GRCh38_imputed_TSS_filter_NaN_regulated.tsv
  - preprocessed file (impute TSS and remove NaN row) 