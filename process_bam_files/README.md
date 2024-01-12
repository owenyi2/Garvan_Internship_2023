# Description
This folder annotates genomic regions listed within a `.bed` file with a signal value of epigenetic features. 
More precisely, it calculates the normalised (RPKM) read counts for each genomic region.

This folder takes in `.bam` files as raw data.  These files can be obtained from ENCODE. 
A bash script `./data/download.sh` is provided in `./data` specifying the exact input files that I used.

# Usage
Modify `config.yaml` to specify location of input (.bam and .bed) files as well as the location to dump results.
Then run `main.py`.


