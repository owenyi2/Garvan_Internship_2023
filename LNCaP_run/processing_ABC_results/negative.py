import pandas as pd
import numpy as np

EnhancerList = pd.read_csv("data/EnhancerList.bed", names = ["chr", "start", "end", "name"], usecols=[0,1,2,3], sep="\t")
GeneList = pd.read_csv("data/GeneList.bed", names = ["chr", "start", "end", "TargetGene"], usecols=[0,1,2,3], sep="\t")
positive_df = pd.read_csv("output/PCHi_C_matched", names = ["chr", "start", "end", "TargetGene"], usecols=[0,1,2,6], sep="\t")

max_dist_from_gene = 750_000
frac_enhancers_sample = 0.05

# for each gene, sample some % of enhancers within certain distance
enh_gene_list = []
for idx, gene in GeneList.iterrows():
    chr, start, end, TargetGene = gene.chr, gene.start, gene.end, gene.TargetGene
     
    if idx % 1000 == 0:
       print(chr)

    eligible_enhancers = EnhancerList[(EnhancerList["chr"] == chr) & (EnhancerList["start"] >= start - max_dist_from_gene) & (EnhancerList["end"] <= end + max_dist_from_gene)]
    enhancers = eligible_enhancers.sample(frac=frac_enhancers_sample, replace = False, random_state=1)
    for _, enhancer in enhancers.iterrows():
        enh_gene_list.append((chr, enhancer.start, enhancer.end, TargetGene))

negative_pairs_df = pd.DataFrame(enh_gene_list, columns = ["chr", "start", "end", "TargetGene"])

# remove the positives from our randomly sampled set to create a purely negative set 
negative_pairs_df = pd.merge(negative_pairs_df, positive_df, on=["chr", "start", "end", "TargetGene"], how='outer', indicator=True).query("_merge == 'left_only'").drop('_merge', axis=1).reset_index(drop=True)

negative_pairs_df.to_csv("output/negative_pairs", header=None, index=None, sep="\t")

