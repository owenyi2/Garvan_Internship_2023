cp ../../LNCaP_run/processing_ABC_results/output/ABC_annotated_candidate_pairs.tsv .
cut -f 1-3 ABC_annotated_candidate_pairs.tsv | tail -n +2 > Candidate_Enhancer_List.bed 
cut -f 4-6 ABC_annotated_candidate_pairs.tsv | tail -n +2 > Candidate_Promoter_List.bed

