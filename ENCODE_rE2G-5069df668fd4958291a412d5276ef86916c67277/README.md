This folder is an archive of https://github.com/EngreitzLab/ENCODE_rE2G frozen at commit 5069df668fd4958291a412d5276ef86916c67277 (14/12/2023)
  - The original repo also used https://github.com/broadinstitute/ABC-Enhancer-Gene-Prediction/ as a submodule. We have it setup as a plain archive frozen at commit cb230435986d8c73f163c8d29b69fa438da82338

This folder calculates the ABC score and overlaps it with a given reference .tsv of candidate EPI pairs. At the momement (Jan 2024), the original repo is currently under development which is why I have copied an archive at this point in time as a bandaid for our purposes so upstream changes don't affect us. When the original repo is stable, we'll have to go migrate this.

The upstream repository handles a superset of tasks that we seek to do and some of our input files are slightly different to theirs. So this archive will include some small plumbing changes that are detailed below
  1. H3K27ac support
     - The upstream repository as it stands has extra functionality for testing out a predictive model for EPI as well. However as it stands, that functionality does not support H3K27ac. Throws error if a H3K27ac path is deteced in the H3K27ac column of ./config/config_biosamples_chr22.tsv. (See ./workflow/rules/utils.smk line 29), This is despite the fact that we may want to use H3K27ac only for the calculation of ABC score only which the ABC submodule does support. We make the following modifications
       - Comment out exception throwing code in .workflow/rules/utils.smk (line 29)
       - Add in H3K27ac file path in ./config/config_biosamples_chr22.tsv
  2. Commenting/Uncommenting workflows used in ./workflow/Snakefile
     - Comment out to disable functionality for running and evaluating model
     - Uncomment in to enable functionality for producing ABC score and features for candidate EPI pairs instead

 
