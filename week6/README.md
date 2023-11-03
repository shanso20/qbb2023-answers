Andrew installed Plink because there were issues with the original commands

plink --noweb  --vcf genotypes.vcf --pca 10

plink --noweb --vcf genotupes.vcf --freq

plink --noweb --vcf genotypes.vcf --linear hide-covar --pheno CB1908_IC50.txt --covar pca.eigenvec --allow-no-sex --out phenotype_gwas_results_1
plink --noweb --vcf genotypes.vcf --linear hide-covar --pheno GS451_IC50.txt --covar pca.eigenvec --allow-no-sex --out phenotype_gwas_results_2

Step 3.4:
In the CB1908 phenotypes, SNP with the top hit fell in a noncoding region of the DIP2B gene, which "showed a negative correlation with immune killer cell infiltration and immune regulatory genes in BRCA subtypes" and expression "was associated with lymph node metastasis". Abnormal expression of these gene could impact the IC50 phenotype observed in the drug. CHR 12, POS 49190411, PVAL 11.086
info source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10064539/

In the GS451 phenotypes, SNP with the top hit fell in the gene ZNF826, which is a zinc finger protein potentially involved in transcriptional regulation. Abnormal expression of this gene could cause abberant transcription when combined with this drug, resulting in the unusual IC50 observed. CHR 19, POS 20372113, PHEN 6.844663962534939.
info course: https://www.genecards.org/cgi-bin/carddisp.pl?gene=ZNF826P
