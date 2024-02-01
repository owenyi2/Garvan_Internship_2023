#!/bin/bash

PCHi_C=./data/PCHi-C_LNCaP_NT_chicago_merge_3Kb.ibed
EnhancerList=./data/EnhancerList.bed
GeneList=./data/GeneList.bed
 
tail -n +2 $PCHi_C | awk '$1 == $5' | bedtools sort -i stdin > tmp/PCHi_C.sorted
bedtools sort -i $EnhancerList > tmp/EnhancerList.sorted.bed
bedtools sort -i $GeneList > tmp/GeneList.sorted.bed

PCHi_C=tmp/PCHi_C.sorted
EnhancerList=tmp/EnhancerList.sorted.bed
GeneList=tmp/GeneList.sorted.bed

GeneDistLeniency=1500
EnhancerDistLeniency=1000

Output=output/PCHi_C_matched

wc -l $PCHi_C
bedtools closest -d -a $PCHi_C -b $GeneList | awk -v GeneDistLeniency=$GeneDistLeniency '$NF < GeneDistLeniency' | cut -f 5-7,10-14 > tmp/PCHi_C.closestGene.bed
wc -l tmp/PCHi_C.closestGene.bed

bedtools sort -i tmp/PCHi_C.closestGene.bed |\
bedtools closest -d -a stdin -b $EnhancerList | awk -v EnhancerDistLeniency=$EnhancerDistLeniency '$NF < EnhancerDistLeniency' | awk '{print $9"\t"$10"\t"$11"\t"$5"\t"$6"\t"$7"\t"$8"\t"$4}' > $Output
wc -l $Output

#head $EnhancerList
#head $GeneList	
