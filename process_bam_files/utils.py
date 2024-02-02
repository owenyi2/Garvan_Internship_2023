import pysam
import pandas as pd
import subprocess
import numpy as np
import os
import shutil

def count_bam(bed_file, bam_file, feature_name):
    alignment = pysam.AlignmentFile(bam_file, "rb")

    bed = pd.read_csv(bed_file, sep="\t", names = ["chrom", "start", "end"])
    bed[feature_name+".counts"] = bed.apply(lambda row: alignment.count(row["chrom"], row["start"], row["end"]), axis = 1)

    return bed

def normalised_counts(bed_file, bam_file, feature_name):
    print("processing", bam_file)
    bed_df = count_bam(bed_file, bam_file, feature_name)
    command = ("samtools", "idxstats", bam_file)

    ps = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = subprocess.check_output(('cut', '-f3'), stdin=ps.stdout).decode("ascii")
    total_counts = sum([int(x) for x in output.split("\n")[:-1]])
    
    bed_df[feature_name+".counts.RPM"] = float(1e6) * bed_df[feature_name+".counts"] / total_counts
    bed_df[feature_name+".counts.RPKM"] = float(1e3) * bed_df[feature_name+".counts.RPM"] / (bed_df.end - bed_df.start)

    return bed_df

def get_distance_between_regions(bed_file_1, bed_file_2):
    bed_df1 = pd.read_csv(bed_file_1, sep="\t", names = ["chrom", "start", "end"])
    bed_df2 = pd.read_csv(bed_file_2, sep="\t", names = ["chrom", "start", "end"])

    assert (bed_df1["chrom"] == bed_df2["chrom"]).all() # assume number of rows and regions on same chromosome in each row

    np.abs((bed_df1["start"] + bed_df1["end"]) // 2, (bed_df2["start"] + bed_df2["end"]) // 2)

# If we want to add qnorm step, this is the code from ABC_predictions
# df[featurecount + ".quantile"] = df[featurecount].rank() / float(len(df)) 
# ...
#  qnorm = pd.read_csv("process_data/EnhancersQNormRef.K562.txt")

# interpfunc = scipy.interpolate.interp1d(qnorm['rank'], qnorm[col], kind='linear', fill_value='extrapolate')
# df[col_dict[col]] = interpfunc((1 - df[col + ".quantile"]) * nRegions).clip(0)

"""

def agg_replicates(bed_df_list, column, agg_fun = np.mean):
    stack = np.vstack([bed_df[column] for bed_df in bed_df_list])
    return np.apply_along_axis(agg_fun, axis=0, arr=stack)

def process_replicates(bed_file, bam_file_list, feature_name):
    bed_df_list = [normalised_counts("test.bed", bam_file, feature_name) for bam_file in bam_file_list]

    bed_df = bed_df_list[0] 
    columns = list(filter(lambda x: feature_name in x, bed_df.columns))
    for column in columns:
        bed_df[column] = agg_replicates(bed_df_list, column)

    # lol we can even wrap this up as a function. Yep but it's still shitty because we are explicitly mentioning normalised counts function

    return bed_df

"""

def get_bam_coverage(bam_file, bed_file, bin_size):
    if os.path.exists("temporary"):
        shutil.rmtree("temporary")
    os.makedirs("temporary")

    bamCoverage_command = ("bamCoverage", "--bam", bam_file, "-bs", str(bin_size), "-of",  "bedgraph", "-o", "temporary/bam_coverage.bedgraph", "--normalizeUsing", "RPKM")
    bam_ps = subprocess.run(bamCoverage_command)

    bedtools_command = ("bedtools", "intersect", "-a", "temporary/bam_coverage.bedgraph", "-b", bed_file, "-loj")
    bed_ps = subprocess.Popen(bedtools_command, stdout=subprocess.PIPE)
    data = subprocess.check_output(("awk", r'$5 !~ /\./'), stdin = bed_ps.stdout).decode("ascii") # remove rows where BAM count is 0 && remove rows where no intersection with relevant regions specified by bed_file

    lines = data.split("\n")

    return_list = []

    bed_df = pd.read_csv(bed_file, sep="\t", names = ["chrom", "start", "end"])
    for idx, row in bed_df.iterrows():
        filter_lines = list(filter(lambda x: f"{row.chrom}\t{row.start}\t{row.end}" in x, lines)) # grab lines that correspond to this region in input bed_file
        
        region_start = row.start // bin_size
        region_end = row.end // bin_size + 1

        region_size = region_end - region_start
        region = np.empty(region_size)
        
        for line in filter_lines:
            fields = line.split("\t")
            start = max(int(fields[1]) // bin_size - region_start, 0)
            end = min(int(fields[2]) // bin_size - region_start, region_end - 1)
            val = float(fields[3])

            region[start:end] = val
            
        return_list.append((f"{row.chrom}\t{row.start}\t{row.end}", region)) 

    return return_list
# a = get_bam_coverage("ENCFF134DLD_chr1.bam", "test.bed", 50)
# print(a)


# bedtools intersect -a temporary/bam_coverage.bedgraph -b test.bed -loj | awk '$5 !~ /\./ && $4 != 0'
