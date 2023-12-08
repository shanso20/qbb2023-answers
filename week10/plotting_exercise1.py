#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt
from statistics import median

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)

# EXERCISE 1.1-------------------------------------------------------------------------------------------------------------------

indeces = []
gtex113jc = []
ylist = []
ylist2 = []
xlist2 = []
for i in range(len(full_design_df)):
	indeces.append(full_design_df.index[i])
for i, j in enumerate(indeces):
	if j == 'GTEX-113JC':
		gtex113jc.append(full_design_df.iloc[i])
for i in gtex113jc[0]:
	ylist.append(i)

for i in range(len(ylist) - 3):
	ylist2.append(ylist[i])

xlist = list(full_design_df)
for i in range(len(xlist) - 3):
	xlist2.append(xlist[i])

x = []
y = []
for i, j in enumerate(ylist2):
	if j == 0.0:
		continue
	else:
		y.append(j)
		x.append(xlist[i])

fig, ax = plt.subplots()
ax.hist(y, bins = 20)
ax.set_title("Expression Distribution in GTEX-113JC")
ax.set_xlabel("log normalized counts")
ax.set_ylabel("# genes")
fig.savefig("Exercise1-1.png")

# EXERCISE 1.2--------------------------------------------------------------------------------------------------------------------------

MXD4 = full_design_df["MXD4"]
SEX = full_design_df["SEX"]

male = []
female = []
for i, j in enumerate(SEX):
	if j == 1:
		male.append(MXD4.iloc[i])
	elif j == 2:
		female.append(MXD4.iloc[i])
maleweights = np.ones(len(male)) / len(male)
femaleweights = np.ones(len(female)) / len(female)

fig1, ax1 = plt.subplots()
ax1.hist(male, alpha = 0.5, weights = maleweights)
ax1.hist(female, alpha = 0.5, weights = femaleweights)
ax1.set_title("Male vs Female Expression of MXD4")
ax1.set_xlabel("log normalized counts")
ax1.set_ylabel("Percent of subjects")
fig1.savefig("Exercise1-2.png")

# EXERCISE 1.3---------------------------------------------------------------------------------------------------------------

AGES = full_design_df["AGE"]
agetypes = []
for i in AGES:
	if i in agetypes:
		continue
	else:
		agetypes.append(i)

ages = {}
for i in range(len(AGES)):
	if AGES.iloc[i] not in ages:
		ages[AGES.iloc[i]] = 1
	else:
		ages[AGES.iloc[i]] += 1

x2 = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]
y2 = [68, 68, 113, 234, 249, 23]

fig2, ax2 = plt.subplots()
ax2.bar(x2, y2)
ax2.set_title("Age Distribution")
ax2.set_xlabel("Age Category")
ax2.set_ylabel("# of Subjects")
fig2.savefig("Exercise1-3.png")

# EXERCISE 1.4-------------------------------------------------------------------------------------------------------------------------

LPXN = full_design_df["LPXN"]
AGE = full_design_df["AGE"]
SEX = full_design_df["SEX"]

LPXN_info = []
LPXN_males = []
LPXN_females = []
male_ages = {}
female_ages = {}
for i, j in enumerate(LPXN):
	LPXN_info.append([j, AGE.iloc[i], SEX.iloc[i]])
for i in LPXN_info:
	if i[-1] == 1:
		LPXN_males.append([i[0], i[1]])
	elif i[-1] == 2:
		LPXN_females.append([i[0], i[1]])
for i in range(len(LPXN_males)):
	if LPXN_males[i][1] not in male_ages:
		male_ages[LPXN_males[i][1]] = [LPXN_males[i][0]]
	else:
		male_ages[LPXN_males[i][1]].append(LPXN_males[i][0])
for i in range(len(LPXN_females)):
	if LPXN_females[i][1] not in female_ages:
		female_ages[LPXN_females[i][1]] = [LPXN_females[i][0]]
	else:
		female_ages[LPXN_females[i][1]].append(LPXN_males[i][0])

ages = ["20-29", "30-39", "40-49", "50-59", "60-69", "70-79"]
male_data = []
for i in ages:
	x = male_ages[i]
	x.sort()
	mid = median(x)
	male_data.append([i, mid])
female_data = []
for i in ages:
	x = female_ages[i]
	x.sort()
	mid = median(x)
	female_data.append([i, mid])

my = [11.290757115811902, 11.219769744497272, 11.244131842527253, 11.331213587080224, 11.35690939913861, 11.470700327588103]
fy = [11.204128451360335, 11.289193232770675, 11.417432508407133, 11.566880702113775, 11.23045598668989, 11.014573484463018]

x_axis = np.arange(len(ages))

fig3, ax3 = plt.subplots(figsize = (10, 7))
ax3.bar(x_axis + 0.2, my, label = "males", width = 0.4)
ax3.bar(x_axis - 0.2, fy, label = "females", width = 0.4)
plt.xticks(x_axis, ages)
ax3.set_title("Median Expression of LPXN Over Time")
ax3.set_xlabel("Age Category")
ax3.set_ylabel("Median Expression")
plt.legend()
fig3.savefig("Exercise1-4.png")