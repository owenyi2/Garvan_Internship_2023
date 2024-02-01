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
print(len(positive_df), "positive pairs")

negative_df["PCHi-C_score"] = np.nan
negative_df["Label"] = False
print(len(negative_df), "negative pairs")

candidate_df = pd.concat([positive_df, negative_df])

print(candidate_df)


merge_df = candidate_df.merge(ABC_df, how="left", on=["chr", "start", "end", "TargetGene"])
merge_df = merge_df[["chr", "start", "end", "TargetGene", "ABC.Score", "PCHi-C_Score", "Label"]]
print("overlap with ABC in positive set")
print(merge_df[merge_df["Label"]]["ABC.Score"].isna().sum())
print("overlap with ABC in negative set")
print(merge_df[~merge_df["Label"]]["ABC.Score"].isna().sum())


merge_df["ABC.Score"] = merge_df["ABC.Score"].fillna(0)

print(merge_df)
print(merge_df.columns)

print("positive set")
print(merge_df[merge_df["Label"]]["ABC.Score"].describe())
print("negative set")
print(merge_df[~merge_df["Label"]]["ABC.Score"].describe())

merge_df.to_csv("output/ABC_annotated_candidate_pairs.tsv", sep="\t")
