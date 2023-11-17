Step 1.1:
Rscript runChicago.R ./raw/PCHIC_Data/GM_rep1.chinput,./raw/PCHIC_Data/GM_rep2.chinput,./raw/PCHIC_Data/GM_rep3.chinput ./output --design-dir ./raw/Design --en-feat-list ./raw/Features/featuresGM.txt --export-format washU_text


Step 1.2:
Do these enrichments make sense to you? Are any surprising? Explain your reasoning briefly for each feature.


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







