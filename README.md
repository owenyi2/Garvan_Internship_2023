* ENCODE_rE2G-5069df668fd4958291a412d5276ef86916c67277
* analysing_output
* encode_e2g_original_dataset
* process_bam_files
* using_ENFORMER
* LNCaP_run

# ENCODE K562 CRIPRi Set

Start from `encode_e2g_original_dataset` to download and preprocess the CRISPRi benchmark dataset. This folder will derive from the preprocessed dataset, various input files for the following workflows
- `process_bam_files`
- `ENCODE_rE2G-5069df668fd4958291a412d5276ef86916c67277`
- `using_ENFORMER`

Run each of the above workflows to produce various features to benchmark e.g. `process_bam_files` for RPKM counts for various epigenetic features, `ENCODE_rE2G-5069df668fd4958291a412d5276ef86916c67277` for ABC score, `using_ENFORMER` for ENFORMER input*grad contribution score

`analysing_output` combines and benchmarks the above features' effectiveness for predicting EPI using the CRISPRi benchmark dataset

# Garvan LNCaP PCHi-C Set

Start with `LNCaP_run` followed by `processing_bam_files` and then `analysing_output`
