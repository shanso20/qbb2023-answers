#!/bin/bash

for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
	echo "Aligning sample:" ${sample}
	bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \
	  sacCer3.fa \
	  ${sample}.fastq > ${sample}.sam
	  samtools sort ${sample}.sam > ${sample}.bam
	  samtools index ${sample}.bam
done

for sample in A01_09 A01_11 A01_23 A01_24 A01_27 A01_31 A01_35 A01_39 A01_62 A01_63
do
	echo ${sample}.bam >> bams.txt
done

freebayes --genotype-qualities -p 1 -f sacCer3.fa -L bams.txt > var.vcf
vcffilter -f "QUAL > 20" var.vcf > filtered_var.vcf
vcfallelicprimitives -k -g filtered_var.vcf > decomposed_var.vcf
snpEff ann R64-1-1.105 decomposed_var.vcf > annotated.vcf 
head -n 100 annotated.vcf > annotated_sample.vcf