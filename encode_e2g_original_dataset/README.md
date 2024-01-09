Downloads, preprocesses and transforms CRISPR interference dataset from [ENCODE-E2G](https://github.com/karbalayghareh/ENCODE-E2G) repo from this [paper](https://www.biorxiv.org/content/10.1101/2023.11.09.563812v1)

Dependencies:
  - pandas

Run `preprocess` first to download and preprocess CRISPR interference dataset from ENCODE-E2G repo

After:
  - Run `for_process_bam_file` to obtain `CandidateEnhancerList.bed` and `CandidatePromoterList.bed` as partial inputs for `process_bam_files`
