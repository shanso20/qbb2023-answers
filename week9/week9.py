#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats import multitest
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import matplotlib.pyplot as plt


# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]
counts_df_normed = np.log2(counts_df_normed + 1)
full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

genes = list(full_design_df)
print(genes)

results_list = []
test_data = []
for i in range(len(genes) - 3):
	model = smf.ols(formula = f'Q("{genes[i]}") ~ SEX', data=full_design_df)
	results = model.fit()
	results_list.append([results, genes[i]])
for i in results_list:
	slope = i[0].params[1]
	pval = i[0].pvalues[1]
	test_data.append([i[1], slope, pval])


fp = open("week9.txt", "w")
fp.write("gene,slope,pval\n")
for i in test_data:
	fp.write(f'{i[0]},{i[1]},{i[2]}\n')
fp.close()

data = pd.read_csv("week9.txt", index_col = 0)
FDR_pvals = multitest.fdrcorrection(data['pval'], alpha = 0.1)

genes = data.index.tolist()
gene_names = []
for i,j in enumerate(FDR_pvals[0]):
	if j == True:
		gene = genes[i]
		gene_names.append(gene)

fp2 = open("genenames.txt", "w")
for i in gene_names:
	fp2.write(i)
	fp2.write("\n")
fp2.close()

# EXERCISE 2----------------------------------------------------------------------------------------------------------------------

dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    n_cpus=4,
)

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
results = stat_res.results_df

fp = open("ddsresults.txt", "w")
results.to_csv("ddsresults.txt")
fp.close()


# # compute Jaccard index = ((number of genes that were significant in steps 1 and 2) / (number of genes that were significant in steps 1 or 2)) * 100%
results = pd.read_csv("ddsresults.txt", index_col = 0)
ddsgenenames= []
NaN = np.nan
ddsgenes = results.index.tolist()
for i,j in enumerate(results["padj"]):
	if j != NaN:
		if j < 0.1:
			gene = ddsgenes[i]
			ddsgenenames.append(gene)

gene_name_fp = open("genenames.txt")
gene_names = []
for i in gene_name_fp:
	i = i.rstrip("\n")
	gene_names.append(i)

sig_and = []
sig_or = []
for i in gene_names:
	if i in ddsgenenames:
		sig_and.append(i)
	else:
		sig_or.append(i)

for i in ddsgenenames:
	if i not in gene_names:
		sig_or.append(i)
JI = ((len(sig_and)/((len(sig_or) + len(sig_and))) * 100))
print(JI)

# # EXERCISE 3----------------------------------------------------------------------------------------------------------------------------
y = -np.log10(results["padj"])
x = results["log2FoldChange"]

sigp = []
x1 = []
for i, j in enumerate(results["padj"]):
	if j < 0.1 and results["log2FoldChange"][i] > 1:
		sigp.append(j + 1e-300)
		x1.append(results["log2FoldChange"][i])
y1 = -np.log10(sigp)

fig, ax = plt.subplots(figsize = (6,6))
ax.scatter(x, y, s = 8)
ax.scatter(x1, y1, s = 8)
ax.set_title("DESeq2 Differential Gene Expression")
ax.set_xlabel("log2FoldChange")
ax.set_ylabel("Adjusted P-value")
plt.show()

