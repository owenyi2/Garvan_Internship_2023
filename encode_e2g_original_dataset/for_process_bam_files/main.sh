tail -n +2 ../preprocess/EPCrisprBenchmark_ensemble_data_GRCh38_imputed_TSS_filter_NaN_regulated.tsv | awk '{print $2"\t"$3"\t"$4}'  > Candidate_Enhancer_List.bed
tail -n +2 ../preprocess/EPCrisprBenchmark_ensemble_data_GRCh38_imputed_TSS_filter_NaN_regulated.tsv | awk '{print $7"\t"int($8)"\t"int($9)}' | bedtools slop -i stdin -l 0 -r 499 -g hg38.chrom.sizes > Candidate_Promoter_List.bed

 
