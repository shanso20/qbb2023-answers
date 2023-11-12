Q1: 
Are the majority of the CpG dinucleotides methylated or unmethylated? 
The majority seem to be methylated.

Q3a:
Bisulfite unique reads: 132466 (2.9908053720974968) %
Bisulfite multi reads: 4296642 (97.0091946279025) %
ONT unique reads: 53346 (1.2263482106157535) %
ONT multi reads: 4296642 (98.77365178938425) %
Total multi: 4296642 (95.85468138657977) %

Q2:
How does using nanopore for methylation calling differ from bisulfite sequencing in terms of coverage? Which method appears better and why?
Nanopore sequencing results in more consistent coverage than bisulfite (coverage distribution is a more narrow peak), however the coverage at this peak is lower than in bisulfite. Thus, since bisulfite sequencing gives a higher average coverage, the bisulfite sequencing is better.

Q3:
What can you infer about the two different approaches and their ability to detect methylation changes? 
While both approaches show similar overall detection of changes in methylation, the variation between the scores is significantly higher in the nanopore sequencing. Thus, bisulfite sequencing appears to be more consistent in its detection of methylation changes.


Q4: What is the effect of tumorigenesis on global methylation patterns?
Tumorigenesis results (mostly) in an increase in global methylation patters, though some loci are demethylated. This makes sense, as in order to grow, tumors need to suppress the expression of many growth-regulatory and tumor-supressor genes, while activating some that allow it to redirect blood flow and gain new abilities.

Q5:
What changes can you observe between the normal and tumor methylation landscape? What do you think the possible effects are of the changes you observed?
The tumor DNMT3A gene seems to be more methylated than the normal gene. This will cause silencing of DNMT3A, which will result in under-methylation (and thus over-expression) of other genes in the genome.

Q6:
What does it mean for a gene to be “imprinted”? 
Imprinting is epigenetic modifications to the genome--such as methylation--that silence one copy of a gene in a diploid organism so that only one copy (from either mother or father) is expressed.

Q7:
What is happening when you select the option to phase the reads? What is required in order to phase the reads?
When I phase the reads, the tracks become split into 3 groups labeled 1, 2, or NONE. In order to phase the reads, there needs to be enough imprinting information (aka, about maternal vs paternal allele expression) to group the reads into clusters.

Q8: 
Can any set of reads be phased? Explain your answer.
No, not any set of reads can be phased. In order to phase the reads, there must be information available about differential expression of the maternal vs paternally-inherited alleles to group the reads into clusters (labeled 1, 2, or none). If the gene or region isn't imprinted and this information is not available, the reads cannot be phased.