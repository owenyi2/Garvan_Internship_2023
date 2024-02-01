#!/bin/bash

# ENCFF134DLD.bam :: DNase
# ENCFF855ZMQ.bam :: H3K4me3
# ENCFF162SWZ.bam :: CTCF
# ENCFF232RQF.bam :: H3K27ac
# ENCFF366MWI.bam :: CAGE 

wget https://www.encodeproject.org/files/ENCFF134DLD/@@download/ENCFF134DLD.bam https://www.encodeproject.org/files/ENCFF855ZMQ/@@download/ENCFF855ZMQ.bam https://www.encodeproject.org/files/ENCFF162SWZ/@@download/ENCFF162SWZ.bam https://www.encodeproject.org/files/ENCFF232RQF/@@download/ENCFF232RQF.bam https://www.encodeproject.org/files/ENCFF366MWI/@@download/ENCFF366MWI.bam

samtools index -M *.bam
 
