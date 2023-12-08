#!/usr/bin/env python

import scanpy as sc
import matplotlib.pyplot as plt

# Read the 10x dataset filtered down to just the highly-variable genes
adata = sc.read_h5ad("variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

sc.pp.neighbors(adata, 10, 40)
sc.tl.leiden(adata)
sc.tl.umap(adata, maxiter = 900)
sc.tl.tsne(adata)

# fig, axes = plt.subplots(ncols=2)
# sc.pl.umap(adata, color = "leiden", ax = axes[0], show=False, title = "UMAP")
# sc.pl.tsne(adata, color = "leiden", ax = axes[1], show=False, title = "t-SNE")
# plt.tight_layout()
# fig.savefig("Exercise1.png")

# EXERCISE 2-----------------------------------------------------------------------------------------------------------------------------------------------

wilcoxon_adata = sc.tl.rank_genes_groups(adata, method = "wilcoxon", groupby='leiden', use_raw = True, copy = True)
logreg_adata = sc.tl.rank_genes_groups(adata, method = "logreg", groupby = "leiden", use_raw = True, copy = True)

# fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()
# sc.pl.rank_genes_groups(wilcoxon_adata, sharey=False, show=False, use_raw=True, ax = ax1, title = "Top 25 Genes Wilcoxon", n_genes = 25)
# sc.pl.rank_genes_groups(logreg_adata, sharey=False, show=False, use_raw=True, ax = ax2, title = "Top 25 Genes LogReg", n_genes = 25)
# plt.tight_layout()
# plt.show()

# EXERCISE 3------------------------------------------------------------------------------------------------------------------------------------------------

open("filtered_data.h5")

leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne

adata.write('filtered_clustered_data.h5')
