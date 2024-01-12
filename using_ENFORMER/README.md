This folder contains a `main.ipynb` notebook which applies the ENFORMER model to extract contribution scores as a feature for predicting Enhancer Promoter Interactions. This notebook is strongly based off of (like literal Ctrl C+V some of the cells + plumbing) https://github.com/google-deepmind/deepmind-research/blob/master/enformer/enformer-usage.ipynb. 

This notebook is best run on Google Colab to access their GPU. 

Borrow preprocessed and cut (columns 1-17 i.e. just Enhancer/Promoter Locations and verdict) EPCrisprBenchmark dataset from ../encode_e2g_original/for_ENCODE_rE2G
```
cp ../encode_e2g_original_dataset/for_ENCODE_rE2G/EPCrisprBenchmark_ensemble_data_reference.tsv .
```

* EPCrisprBenchmark_ensemble_data_reference.tsv :: list of candidate EPI pairs
* using_ENFORMER.ipynb :: Run this on Google Colab (or locally if GPU available)
* ENFORMER_output_0.tsv :: Output file from `using_ENFORMER.ipynb`. Contains ENFORMER scores for the columns that could be annotated by ENFORMER (i.e. distance to TSS within half the window width of 114kbp) 
* analysing_ENFORMER_output.ipynb :: standalone check of usefulness of ENFORMER score in isolation


 
