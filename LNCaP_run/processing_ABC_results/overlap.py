import pandas as pd
import numpy as np

ABC_results_path = "data/EnhancerPredictionsAllPutative.tsv.gz"
PCHi_C_path = "output/PCHi_C_matched"
negative_path = "output/negative_pairs"

PCHi_C_df = pd.read_csv(PCHi_C_path, sep="\t", names=["chr", "start", "end", "chrTSS", "startTSS", "endTSS", "TargetGene", "PCHi-C_Score"])
#print(PCHi_C_df)

ABC_df = pd.read_csv(ABC_results_path, sep="\t")
#print(ABC_df)
print(len(ABC_df))

negative_df = pd.read_csv(negative_path, sep="\t", names=["chr", "start", "end", "TargetGene"])

# concat positive and negative pairs
positive_df = PCHi_C_df[["chr", "start", "end", "TargetGene", "PCHi-C_Score"]]
positive_df["Label"] = True
num_positive = len(positive_df)
print(num_positive, "positive pairs")

negative_df["Label"] = False
num_negative = len(negative_df)
print(num_negative, "negative pairs")

candidate_df = pd.concat([positive_df, negative_df])
print(candidate_df)

# merge in ABC scores
merge_df = candidate_df.merge(ABC_df, how="left", on=["chr", "start", "end", "TargetGene"])
merge_df = merge_df[["chr", "start", "end", "TargetGene", "ABC.Score", "PCHi-C_Score", "Label"]]

# merge in TSS coords
geneTSS_df = pd.read_csv("../ABC-Enhancer-Gene-Prediction-1.0.0/reference/hg38/CollapsedGeneBounds.hg38.TSS500bp.bed", sep="\t", names = ["chrTSS","startTSS", "endTSS", "TargetGene"], usecols=[0,1,2,3], skiprows=1)
merge_df = merge_df.merge(geneTSS_df, how="left", on = ["TargetGene"])

# distance to TSS
merge_df["distanceToTSS"] = np.abs((merge_df["start"]+merge_df["end"])//2 - (merge_df["startTSS"] + merge_df["endTSS"])//2)
merge_df = merge_df[["chr", "start", "end", "chrTSS", "startTSS", "endTSS", "TargetGene", "distanceToTSS", "ABC.Score", "PCHi-C_Score", "Label"]] # reorder columns

# % overlap with ABC score
print("overlap with ABC in positive set")
print(1 - merge_df[merge_df["Label"]]["ABC.Score"].isna().sum()/num_positive)
print("overlap with ABC in negative set")
print(1 - merge_df[~merge_df["Label"]]["ABC.Score"].isna().sum()/num_negative)

# NA
merge_df["ABC.Score"] = merge_df["ABC.Score"].fillna(0)
print("missing values")
print(merge_df.isna().any())

print(merge_df)
print(merge_df.columns)

print("positive set")
print(merge_df[merge_df["Label"]]["ABC.Score"].describe())
print("negative set")
print(merge_df[~merge_df["Label"]]["ABC.Score"].describe())

merge_df.to_csv("output/ABC_annotated_candidate_pairs.tsv", index=None, sep="\t")
