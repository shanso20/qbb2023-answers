#!/usr/bin/env python
import matplotlib.pyplot as plt
import math
import numpy as np

# in command line: brew install plink
pca1_list = []
pca2_list =[]
for line in open("pca.eigenvec"):
	fields = line.rstrip('\n').split(" ")
	pca1 = fields[2]
	pca2 = fields[3]
	pca1_list.append(float(pca1))
	pca2_list.append(float(pca2))

AF_info = []
for line in open("plink.frq"):
	fields = line.rstrip("\n").split(" ")
	#print(fields)
	for i in fields:
		if i.startswith("0"):
			AF_info.append(float(i))

master_1 = []
pvals = []
for line in open("phenotype_gwas_results_1.assoc.linear"):
	fields = line.rstrip("\n").split(" ")
	temp_fields = []
	for i in fields:
		if i == "":
			continue
		else:
			temp_fields.append(i)
	if temp_fields[0] == "CHR":
		continue
	master_1.append([temp_fields[0], int(temp_fields[2]), -math.log10(float(temp_fields[-1]))])
	pvals.append(-math.log10(float(temp_fields[-1])))

# for i in master_1:
# 	if i[2] > 11:
# 		print(i)
# max = CHR 12, POS 49190411, PVAL 11.086


data = []
for line in open("genotypes.vcf"):
	fields = line.rstrip("\n").split("\t")
	if fields[0] == "12" and fields[1].startswith("49190411"):
		data.append(fields[9:])
genotypes = data[0]

phenotypes = []
for line in open("CB1908_IC50.txt"):
	fields = line.rstrip("\n").split("\t")
	phenotypes.append(fields[2])
phenotypes = phenotypes[1:]


combined = []
for i in range(len(genotypes)):
	combined.append([genotypes[i], phenotypes[i]])


hom_dom = []
het = []
hom_rec = []
for i in combined:
	if i[0] == "./.":
		continue
	elif i[0] == "0/0":
		hom_dom.append([i[0], float(i[1])])
	elif i[0] == "0/1" and i[1] != "NA":
		het.append([i[0], float(i[1])])
	elif i[0] == "1/1":
		hom_rec.append([i[0], float(i[1])])

homdom_phen = []
for x in hom_dom:
	homdom_phen.append(x[1])
het_phen = []
for x in het:
	het_phen.append(x[1])
homrec_phen = []
for x in hom_rec:
	homrec_phen.append(x[1])

master_2 = []
for line in open("phenotype_gwas_results_2.assoc.linear"):
	fields = line.rstrip("\n").split(" ")
	temp_fields = []
	for i in fields:
		if i == "":
			continue
		else:
			temp_fields.append(i)
	if temp_fields[0] == "CHR":
		continue
	master_2.append([temp_fields[0], int(temp_fields[2]), -math.log10(float(temp_fields[-1]))])
master_1.sort()	
master_2.sort()


# for i in master_2:
# 	if i[2] > 6.5:
# 		print(i)
# max = CHR 19, POS 20372113, PHEN 6.844663962534939

colors_1 = []
for i in master_1:
	if i[2] >= 5:
		color = "red"
	else:
		color = "blue"
	colors_1.append(color)

colors_2 = []
for i in master_2:
	if i[2] >= 5:
		color = "red"
	else:
		color = "blue"
	colors_2.append(color)

fig1, ax = plt.subplots(2, 2, figsize = [10,9])

ax[0,0].scatter(pca1_list, pca2_list)
ax[0,1].hist(AF_info, bins = 20)
ax[1,0].scatter(range(len(master_1)), [x[2] for x in master_1], c = colors_1)
ax[1,1].scatter(range(len(master_2)), [x[2] for x in master_2], c = colors_2)

ax[0,0].set_title("PCA1 vs PCA2")
ax[0,0].set_xlabel("PCA1")
ax[0,0].set_ylabel("PCA2")

ax[0,1].set_title("Allele Frequency Spectrum")
ax[0,1].set_xlabel("Allele Frequency")
ax[0,1].set_ylabel("Frequency")

ax[1,0].set_title("GWAS Manhattan for CB1908")
ax[1,0].set_xlabel("SNP order")
ax[1,0].set_ylabel("-log10(Pval)")

ax[1,1].set_title("GWAS Manhattan for GS451")
ax[1,1].set_xlabel("SNP order")
ax[1,1].set_ylabel("-log10(Pval)")

labels = ["0/0", "0/1", "1/1"]
fig2, ax2 = plt.subplots()
ax2.boxplot([homdom_phen, het_phen, homrec_phen])
ax2.set_title("Genotype Distribution CB1908 Lowest Pval SNP")
ax2.set_xlabel("Genotype")
ax2.set_ylabel("IC50")
ax2.set_xticklabels(labels)

# plt.show()
# fig2.savefig("week6_boxplot.png")
# fig1.savefig("week6.png")