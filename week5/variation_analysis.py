#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

fields_list = []
for line in open("annotated.vcf"):
	if line.startswith('#'):
		continue
	fields = line.rstrip('\n').split('\t')
	fields_list.append(fields)

data = []
for line in fields_list:
	info = line[7]
	info = info.split(";")
	info_dict = {}
	for item in info:
		split_item = item.split("=")
		key = split_item[0]
		value = split_item[1]
		info_dict[key] = value
	line[7] = info_dict
	data.append(line)

DP_list = []
GQ_list = []
AF_list = []
Pred_eff = {}
for line in data:
	info = line[7]
	AF_info = info["AF"]
	if "," in AF_info:
		AF_info = AF_info.split(",")
		AF_list.append(float(AF_info[0]))
		AF_list.append(float(AF_info[1]))
	else:
		AF_list.append(float(AF_info))
	Pred_info = info["ANN"]
	Pred_info = Pred_info.split("|")
	key = Pred_info[1]
	if key not in Pred_eff:
		Pred_eff[key] = 0
	Pred_eff[key] += 1
	x = 9
	while x <= 18:
		if line[x].startswith("0") or line[x].startswith("1"):
			sample_data = str(line[x])
			sample_data = sample_data.split(":")
			DP_data = sample_data[2].split(",")
			GQ_data = float(sample_data[1])
			GQ_list.append(GQ_data)
			for i in DP_data:
				DP_list.append(int(i))
		x += 1

fig1, ax = plt.subplots(2, 2, figsize = [10,7])
ax[0,0].hist(np.log10(np.array(DP_list)), bins = 20)
ax[1,0].hist(GQ_list)
ax[0,1].hist(AF_list)

ax[0,0].set_title( "Read Depth Distribution" )
ax[0,0].set_xlabel( "Log10(Read Depth)")
ax[0,0].set_ylabel( "Frequency")

ax[1,0].set_title("Genotype Quality Distribution")
ax[1,0].set_xlabel( "Genotype Quality")
ax[1,0].set_ylabel( "Frequency")

ax[0,1].set_title("Allele Frequency Spectrum")
ax[0,1].set_xlabel( "Allele Frequency")
ax[0,1].set_ylabel( "Frequency")

ax[1,1].bar(list(Pred_eff.keys()), list(Pred_eff.values()))
ax[1,1].set_xticklabels(list(Pred_eff.keys()), rotation = 45, ha = "right", fontsize = 5)
ax[1,1].set_ylabel("Frequency")
ax[1,1].set_title("Predicted Effects")

plt.tight_layout()
fig1.savefig( "Week_5_Ex_3.png" )
plt.show()