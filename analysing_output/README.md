# K562_crispri

Input files:
* enh_feature.tsv
* pro_feature.tsv
* EPCrisprBenchmark_ensemble_data_GRCh38.K562_ActivityOnly_features_NAfilled.tsv
* ENFORMER_output_0.tsv

Input files are copied directly over from other workflows
```
cp ../ENCODE_rE2G-5069df668fd4958291a412d5276ef86916c67277/results/K562/EPCrisprBenchmark_ensemble_data_GRCh38.K562_ActivityOnly_features_NAfilled.tsv.gz K562_crispri 
cp ../process_bam_files/K562_crispri/results/* K562_crispri
cp ../using_ENFORMER/ENFORMER_output* K562_crispri
```

Process:
* K562_crispri/main.ipynb

# LNCaP_PCHi_C

Input files:
* enh_feature.tsv
* pro_feature.tsv
* ABC_annotated_candidate_pairs.tsv

Input files are copied directly from other workflows
```
cp ../LNCaP_run/processing_ABC_results/output/ABC_annotated_candidate_pairs.tsv LNCaP_PCHi_C
cp ../process_bam_files/LNCaP/results/* LNCaP_PCHi_C
```

Process:
* main.ipynb

# graphs_for_poster.ipynb
* uses files from above folders
