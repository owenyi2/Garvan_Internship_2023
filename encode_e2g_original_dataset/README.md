Downloads, preprocesses and transforms CRISPR interference dataset from [ENCODE-E2G](https://github.com/karbalayghareh/ENCODE-E2G) repo from this [paper](https://www.biorxiv.org/content/10.1101/2023.11.09.563812v1)

Dependencies:
  - pandas

Run `./preprocess` first to download and preprocess CRISPR interference dataset from ENCODE-E2G repo
  - entry point: `./preprocess/main.ipynb`
    - downloads original CRISPR dataset and imputes/filter missing values. More details described in `./preprocess/main.ipynb`

After:
  - Run `./for_process_bam_files` to obtain `CandidateEnhancerList.bed` and `CandidatePromoterList.bed` as partial inputs for `process_bam_files`
    - entry point: `./for_process_bam_files/main.py`
      - from preprocessed input, extracts out candidate Enhancer and Promoter regions into .bed files
  - Run `./for_ENCODE_rE2G` to obtain `EPCrisprBenchmark_ensemble_data_reference.tsv`
    - entry point: `./cut_columns.sh`
      - from preprocessed input, extracts necessary columns to feed into ENCODE-rE2G workflow
