This folder annotates genomic regions listed within a `.bed` file with a signal value of epigenetic features. 
More precisely, it calculates the normalised (RPKM) read counts for each genomic region.

This folder takes in `.bam` files as raw data.  These files can be obtained from ENCODE. 
A bash script is provided describing input files that I used.

This is shitty practise but the file locations are hard-coded in `main.py`, so go edit `main.py` first. 

* data
  * 
* data_pipeline.yaml
* main.py
* utils.py
