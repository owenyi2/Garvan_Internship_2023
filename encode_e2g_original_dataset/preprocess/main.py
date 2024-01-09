import pandas as pd

df = pd.read_csv("EPCrisprBenchmark_ensemble_data_GRCh38.K562_ENCDO000AAD_ENCFF325RTP_DNaseOnly_features_NAfilled.tsv", sep="\t")

df.loc[df[["startTSS", "endTSS"]].isna().any(axis=1), "startTSS"] = 12734774
df.loc[df[["startTSS", "endTSS"]].isna().any(axis=1), "endTSS"] = 12734775 #impute C19orf43 TSS based on Gasperini dataset

df = df.drop(df[df["Regulated"].isna()].index) # remove the 1 row with missing `Regulated` value
df.to_csv("EPCrisprBenchmark_ensemble_data_GRCh38_imputed_TSS_filter_NaN_regulated.tsv", sep="\t", index=None)