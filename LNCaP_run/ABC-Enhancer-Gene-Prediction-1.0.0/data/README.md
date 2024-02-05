`LNCaP_bam_files` is a symlink to a folder containg relevant .bam files. The contents are listed below
BGI20101108_LNCaP_CTCF.bam      Marcel_LNCaP_H3K4me3.bam      sort_index.sh                  USC20130125_LNCaP_H3K27ac.bam.bai  USC20140207_DNase_LNCaP_24U.bam.bai
BGI20101108_LNCaP_CTCF.bam.bai  Marcel_LNCaP_H3K4me3.bam.bai  USC20130125_LNCaP_H3K27ac.bam  USC20140207_DNase_LNCaP_24U.bam

The contents of `sort_index.sh` is provided below
```
for f in *.bam; do samtools sort --threads 12 $f -o tmpfile && mv tmpfile $f; samtools index $f; done
```

`avg_hic_juicebox` is a symlink to a folder containing average hic juicebox output. It can be downloaded from [broad institute average hic](ftp://ftp.broadinstitute.org/outgoing/lincRNA/average_hic/average_hic.v2.191020.tar.gz). Details about average hic dataset can be found here https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9153265/ 
