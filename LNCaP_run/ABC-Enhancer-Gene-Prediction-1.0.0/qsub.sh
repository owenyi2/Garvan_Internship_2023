source ./setup.sh
source activate /home/oweyi/micromamba/envs/abc-env-1

snakemake -p  --cores 12

# note to self: use following command to qsub this `qsub -cwd -l mem_requested=32G qsub.sh -w e`
