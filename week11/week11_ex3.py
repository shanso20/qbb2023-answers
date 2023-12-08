#!/usr/bin/env python

import scanpy as sc
import matplotlib.pyplot as plt

adata = sc.read_h5ad("filtered_clustered_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

# markers = ["FCGR3A", "GNLY", "CD79A"]

# fig, axes= plt.subplots(ncols=6, figsize = (15, 5))
# sc.pl.umap(adata, color = "FCGR3A", ax = axes[0], show=False, title = "FCGR3A")
# sc.pl.tsne(adata, color = "FCGR3A", ax = axes[1], show=False, title = "FCGR3A")

# sc.pl.umap(adata, color = "GNLY", ax = axes[2], show=False, title = "GNLY")
# sc.pl.tsne(adata, color = "GNLY", ax = axes[3], show=False, title = "GNLY")

# sc.pl.umap(adata, color = "CD79A", ax = axes[4], show=False, title = "CD79A")
# sc.pl.tsne(adata, color = "CD79A", ax = axes[5], show=False, title = "CD79A")

# plt.tight_layout()
# plt.show()
# fig.savefig("Exercise3-2.png")

# EXERCISE 3.3-------------------------------------------------------------------------------------------------------------------------------------------

newnames = [
	4, "Monocytes",
	5, "NK",
	2, "B-cell",
	1, "1",
	3, "3",
	6, "6",
	7, "7",
	0, "0"]

# newnames = {4: "Monocytes", 5: "NK", 2: "B-cell"}
adata.rename_categories("leiden", ["0", "1", "B-cell", "3", "Monocytes", "NK", "6", "7"])

fig, axes = plt.subplots(ncols = 2)
sc.pl.umap(adata, color = "leiden", ax = axes[0], show=False, title = "UMAP")
sc.pl.tsne(adata, color = "leiden", ax = axes[1], show=False, title = "TSNE")
plt.tight_layout()
plt.show()
fig.savefig("Exercise3-3.png")