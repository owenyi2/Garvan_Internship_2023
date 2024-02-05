# Description
This folder annotates genomic regions listed within a `.bed` file with a signal value of epigenetic features. 
More precisely, it calculates the normalised (RPKM) read counts for each genomic region.

This folder is used twice. Once for K562 CRISPRi dataset and once for LNCaP PCHi-C dataset

## K562_crispri
This folder takes in `.bam` files as raw data.  These files can be obtained from ENCODE. 
A bash script `./K562_crispri/data/download.sh` is provided specifying the exact input files from ENCODE that I used.

## LNCaP
`LNCaP/data` is a symlink to a folder containg relevant .bam files. The contents are listed below
BGI20101108_LNCaP_CTCF.bam      Marcel_LNCaP_H3K4me3.bam      sort_index.sh                  USC20130125_LNCaP_H3K27ac.bam.bai  USC20140207_DNase_LNCaP_24U.bam.bai
BGI20101108_LNCaP_CTCF.bam.bai  Marcel_LNCaP_H3K4me3.bam.bai  USC20130125_LNCaP_H3K27ac.bam  USC20140207_DNase_LNCaP_24U.bam

The contents of `sort_index.sh` is provided below
```
for f in *.bam; do samtools sort --threads 12 $f -o tmpfile && mv tmpfile $f; samtools index $f; done
```

# Usage
Modify `config.yaml` to specify location of input (.bam and .bed) files as well as the location to dump results.
Then run `main.py`.

Note: Provided here are two config files. `config_K562.yaml` and `config.yaml`. `config.yaml` is the one in use currently and contains the configuration for LNCaP folder. 
