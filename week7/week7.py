#!/usr/bin/env python
import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn

# bis_pos = []
# bis_cov = []
# bis_scores = []
# bis_info = []
# for line in open("bisulfite.cpg.chr2.bedgraph"):
# 	fields = line.rstrip('\n').split("\t")
# 	bis_pos.append(fields[1])
# 	bis_cov.append(int(fields[-1]))
# 	bis_info.append(fields)

# ONT_pos = []
# ONT_cov = []
# ONT_scores = []
# ONT_info = []
# for line in open("ONT.cpg.chr2.bedgraph"):
# 	fields = line.rstrip('\n').split("\t")
# 	ONT_pos.append(fields[1])
# 	ONT_cov.append(int(fields[-1]))
# 	ONT_info.append(fields)


# bis_pos_set = set(bis_pos)
# ONT_pos_set = set(ONT_pos)


# just_bis = set()
# just_ONT = set()
# shared = set()

# for i in bis_pos_set:
# 	if i in ONT_pos_set:
# 		shared.add(i)
# 	else:
# 		just_bis.add(i)
# for i in ONT_pos_set:
# 	if i in shared:
# 		continue
# 	else:
# 		just_ONT.add(i)

# for i in bis_info:
# 	if i[1] in shared:
# 		bis_scores.append(float(i[-2]))
# for i in ONT_info:
# 	if i[1] in shared:
# 		ONT_scores.append(float(i[-2]))

# # print(f"Bisulfite unique reads: {len(just_bis)} ({len(just_bis) / len(bis_pos_set) * 100}) %")
# # print(f"Bisulfite shared reads: {len(shared)} ({len(shared) / len(bis_pos_set) * 100}) %")
# # print(f"ONT unique reads: {len(just_ONT)} ({len(just_ONT) / len(ONT_pos_set) * 100}) %")
# # print(f"ONT shared reads: {len(shared)} ({len(shared) / len(ONT_pos_set) * 100}) %")
# # print(f"Total shared: {len(shared)} ({len(shared) / (len(shared) + len(just_bis) + len(just_ONT)) * 100})")

# fig1, ax1 = plt.subplots()


# ax1.hist(bis_cov, bins = 100, range = (0,100), alpha = 0.5, label = "Bisulfite")
# ax1.hist(ONT_cov, bins = 100, range = (0,100), alpha = 0.5, label = "Nanopore")

# ax1.set_title("Bisulfite vs Nanopore Sequencing Coverage Distribution")
# ax1.set_xlabel("Coverage")
# ax1.set_ylabel("Frequency")

# ax1.set_xlabel("Coverage")
# ax1.set_ylabel("Frequency")

# ax1.legend()

# plt.show()
# fig1.savefig("Bisulfite vs Nanopore Sequencing Coverage")

# numpybisscores = np.array(bis_scores)
# numpyONTscores = np.array(ONT_scores)
# numpyhist = np.histogram2d(numpybisscores, numpyONTscores, bins = 100)
# print(np.corrcoef(numpybisscores, numpyONTscores))
# numpyhist = np.log10(numpyhist[0] + 1)

# fig2, ax2 = plt.subplots()
# ax2.imshow(numpyhist, origin = "lower")
# ax2.set_title(f"CpG Methylation Scores Relationships, R = {np.corrcoef(numpybisscores, numpyONTscores)[0][1] : 0.3f}")
# ax2.set_xlabel("Bisulfite Scores")
# ax2.set_ylabel("Nanopore Scores")
# plt.show()
# fig2.savefig("CpG Methylation Scores Relationships")

#Part 3d:

Nbis_info = []
Nbis_set = set()
for line in open("normal.bisulfite.chr2.bedgraph"):
	fields = line.rstrip('\n').split("\t")
	Nbis_info.append(fields)
	Nbis_set.add(fields[1])
Tbis_info = []
Tbis_set = set()
for line in open("tumor.bisulfite.chr2.bedgraph"):
	fields = line.rstrip('\n').split("\t")
	Tbis_info.append(fields)
	Tbis_set.add(fields[1])

NvTbis_shared = set()
for i in Nbis_set:
	if i in Tbis_set:
		NvTbis_shared.add(i)

Nbis_scores = []
Tbis_scores = []
NvTscores_diff = []
for i in Nbis_info:
	if i[1] in NvTbis_shared:
		Nbis_scores.append(float(i[-2]))
for i in Tbis_info:
	if i[1] in NvTbis_shared:
		Tbis_scores.append(float(i[-2]))
for i in range(len(Nbis_scores)):
	diff = Nbis_scores[i] - Tbis_scores[i]
	if diff != 0.0:
		NvTscores_diff.append(diff)
NvTscores_diff = np.array(NvTscores_diff)

Nont_info = []
Nont_set = set()
for line in open("normal.ONT.chr2.bedgraph"):
	fields = line.rstrip('\n').split("\t")
	Nont_info.append(fields)
	Nont_set.add(fields[1])
Tont_info = []
Tont_set = set()
for line in open("tumor.ONT.chr2.bedgraph"):
	fields = line.rstrip('\n').split("\t")
	Tont_info.append(fields)
	Tont_set.add(fields[1])

NvTont_shared = set()
for i in Nont_set:
	if i in Tont_set:
		NvTont_shared.add(i)

Nont_scores = []
Tont_scores = []
NvTscores2_diff = []
for i in Nont_info:
	if i[1] in NvTont_shared:
		Nont_scores.append(float(i[-2]))
for i in Tont_info:
	if i[1] in NvTont_shared:
		Tont_scores.append(float(i[-2]))
for i in range(len(Nont_scores)):
	diff = Nont_scores[i] - Tont_scores[i]
	if diff != 0.0:
		NvTscores2_diff.append(diff)
NvTscores2_diff = np.array(NvTscores2_diff)

print(Nont_scores[0:10])
print(Tont_scores[0:10])

print(np.corrcoef(NvTscores_diff))

seaborn.violinplot(NvTscores_diff)
seaborn.violinplot(NvTscores2_diff)
plt.show()