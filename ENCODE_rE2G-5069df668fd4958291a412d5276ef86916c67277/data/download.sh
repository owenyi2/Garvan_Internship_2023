# wget https://www.encodeproject.org/files/ENCFF860XAE/@@download/ENCFF860XAE.bam https://www.encodeproject.org/files/ENCFF790GFL/@@download/ENCFF790GFL.bam

for f in *.bam; do samtools sort --threads 12 $f -o tmpfile && mv tmpfile $f; samtools index $f; done


 

