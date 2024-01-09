from functools import reduce
import pandas as pd
import yaml

from utils import normalised_counts



with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

    features = config["features"]
    enhancer_list = config["enhancer_list"]
    promoter_list = config["promoter_list"]
    results = config["results_dir"]

print(features)
print(enhancer_list, promoter_list)

print("processing features")
enh_feature_df_list = [normalised_counts(enhancer_list, bam_file, feature) for (feature, bam_file) in features.items()]
pro_feature_df_list = [normalised_counts(promoter_list, bam_file, feature) for (feature, bam_file) in features.items()]

print("merging features")
enh_overall_feature_df = reduce(lambda df0, df1: pd.concat([df0, df1.drop(["chrom", "start", "end"], axis=1)], axis=1), enh_feature_df_list)
pro_overall_feature_df = reduce(lambda df0, df1: pd.concat([df0, df1.drop(["chrom", "start", "end"], axis=1)], axis=1), pro_feature_df_list)

enh_overall_feature_df.to_csv(f"{results}/enh_feature.tsv", sep="\t", index=False)
pro_overall_feature_df.to_csv(f"{results}/pro_feature.tsv", sep="\t", index=False)
