Step 1.1:
Rscript runChicago.R ./raw/PCHIC_Data/GM_rep1.chinput,./raw/PCHIC_Data/GM_rep2.chinput,./raw/PCHIC_Data/GM_rep3.chinput ./output --design-dir ./raw/Design --en-feat-list ./raw/Features/featuresGM.txt --export-format washU_text


Step 1.2:
Do these enrichments make sense to you? Are any surprising? Explain your reasoning briefly for each feature.
Most of the feature overlap data makes sense to me. H3K4me1, H3K27me3, and H3K9me3 are markers of heterochromatin, so DNA is tightly wound around histones with these markers. When fragmented, I'd assume many or most fragments in these regions to contain a marked histone, since they do not leave many open areas to be cut. I am, however, surprised that the amounts of significant overlaps with H3K27me3 is less than random for this very reason, and I am surprised by the extremely large enrichment of H3K4me1. I am not surprised by the enrichment of CTCF, as this feature's function is to bring distant regions of DNA closer together to form loops. H3K4me3 and H3K27me3 are markers of open chromatin, and the increased flexibility of these regions explain why there would be an enrichment in overlaps with this feature as well.


Step 2.2:
The 6 top-scoring interactions between two promoters:
chr20	44438565	44565593	.	1000	34.77	.	0	chr20	44562442	44565593	PCIF1	+	chr20	44438565	UBE2C	+
chr20	44438565	44607204	.	986	34.29	.	0	chr20	44596299	44607204	FTLP1;ZNF335	+	chr20	44438565	UBE2C	+
chr21	26837918	26939577	.	978	34.02	.	0	chr21	26837918	26842640	snoU13	+	chr21	26926437	MIR155HG	+
chr20	44452862	44565593	.	974	33.89	.	0	chr20	44562442	44565593	PCIF1	+	chr20	44452862	SNX21;TNNC2	+
chr20	24972345	25043735	.	973	33.84	.	0	chr20	24972345	24985047	APMAP	+	chr20	25036380	ACSS1	+
chr20	17660712	17951709	.	973	33.85	.	0	chr20	17946510	17951709	MGME1;SNX5	+	chr20	17660712	RRBP1	+

The 6 top-scoring interactions between a promoter and an enhancer:
chr21	26797667	26939577	.	952	33.13	.	0	chr21	26926437	26939577	MIR155HG	+	chr21	26797667	.	-
chr20	55957140	56074932	.	928	32.29	.	0	chr20	55957140	55973022	RBM38;RP4-800J21.3	+	chr20	56067414	.	-
chr21	26790966	26939577	.	838	29.17	.	0	chr21	26926437	26939577	MIR155HG	+	chr21	26790966	.	-
chr20	5585992	5628028	.	830	28.88	.	0	chr20	5585992	5601172	GPCPD1	+	chr20	5625693	.	-
chr21	26793954	26939577	.	754	26.23	.	0	chr21	26926437	26939577	MIR155HG	+	chr21	26793954	.	-
chr20	5515866	5933156	.	750	26.08	.	0	chr20	5929472	5933156	MCM8;TRMT6	+	chr20	5515866	.	-


Step 2.3:
Does it make sense for this gene to be interacting with enhancers in GM12878? Explain.

- Summary for MIR155HG: This gene represents a microRNA host gene. The long RNA transcribed from this gene is expressed at high levels in lymphoma and may function as an oncogene (from NCBI)
	Yes, it makes sense that this gene would be interacting with enhancers in GM12878, as it has been identified as an oncogene highly expressed in lymphoma. A B-cell human cell line such as the one at the focus of this homework would need behave with some cancer-like qualities in order to be passaged and studied, and overlap of this gene with enhancers would lead to increased expression and, thus, such qualities.

-Summary for RBM38;RP4-800J21.3: Enables mRNA 3'-UTR binding activity. Involved in DNA damage response, signal transduction by p53 class mediator; negative regulation of cell population proliferation; and regulation of RNA metabolic process. Located in cytosol and nucleus (from NCBI)
	It does not make much sense to me that this gene interacts with enhancers in GM12878. As a negative cell population regulator, I would expect this to be downregulated in a cell line used for research, since such lines need unnatural, cancer-like proliferative properties.







