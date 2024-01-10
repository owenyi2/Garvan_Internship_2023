This folder contains a `main.ipynb` notebook which applies the ENFORMER model to extract contribution scores as a feature for predicting Enhancer Promoter Interactions. This notebook is strongly based off of (like literal Ctrl C+V some of the cells + plumbing) https://github.com/google-deepmind/deepmind-research/blob/master/enformer/enformer-usage.ipynb. 

This notebook is best run on Google Colab to access their GPU. 

Borrow preprocessed and cut (columns 1-17 i.e. just Enhancer/Promoter Locations and verdict) EPCrisprBenchmark dataset from ../encode_e2g_original/for_ENCODE_rE2G
cp ../encode_e2g_original_dataset/for_ENCODE_rE2G/EPCrisprBenchmark_ensemble_data_reference.tsv .

* EPCrisprBenchmark_ensemble_data_reference.tsv
