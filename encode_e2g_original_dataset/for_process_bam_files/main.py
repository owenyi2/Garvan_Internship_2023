import pandas as pd

df = pd.read_csv("../preprocess/EPCrisprBenchmark_ensemble_data_GRCh38_imputed_TSS_filter_NaN_regulated.tsv", sep="\t")

enh_col = ["chrom", "chromStart", "chromEnd"]
pro_col = ["chrTSS", "startTSS", "endTSS"]

df[enh_col].to_csv("Candidate_Enhancer_List.bed", header=False, index=False, sep="\t")
df[pro_col].to_csv("Candidate_Promoter_List.bed", header=False, index=False, sep="\t")
