#!/usr/bin/env python
import pandas as pd 

data = pd.read_csv("/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_dnm.csv")
#print(data)

#print(data["Proband_id"])
#print(data["Phase_combined"])

maternal = []
paternal = []
for x in data.index:
	#print(data.loc[x, "Phase_combined"])
	if data.loc[x, "Phase_combined"] == "mother":
		maternal.append(data.loc[x, "Proband_id"])
	elif data.loc[x, "Phase_combined"] == "father":
		paternal.append(data.loc[x, "Proband_id"])
#print(maternal)

#print(len(maternal))
#print(len(paternal))

# make a dictionary where key = proband id and values = [# maternal, # paternal]
MvP = {}

for pbid in maternal:
	if pbid not in MvP:
		MvP[pbid] = [0,0]
	MvP[pbid][0] += 1 

for pbid in paternal:
	if pbid not in MvP:
		MvP[pbid] = [0,0]
	MvP[pbid][1] += 1 

# print(MvP)	

# PART 1.3--------------------------------------------------------------------------------------------------------------------------------------

MvPDF = pd.DataFrame.from_dict(MvP, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])

# PART 1.4--------------------------------------------------------------------------------------------------------------------------------------

#print(MvPDF)

age_data = pd.read_csv("/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_parental_age.csv", index_col = 0)
#print(age_data)

# PART 1.5--------------------------------------------------------------------------------------------------------------------------------------

merged = pd.concat([MvPDF, age_data], axis = 1)
#print(merged)

# EXERCISE 2 ####################################################################################################################################

import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax1.set_title( "Maternal Age vs DNM" )
ax1.set_xlabel( "age of mother")
ax1.set_ylabel( "# maternal DNMs")
ax1.scatter(merged["Mother_age"], merged["maternal_dnm"])
fig.savefig( "Ex2_a.png" )
#plt.show()

fig, ax2 = plt.subplots()
ax2.set_title( "Paternal Age vs DNM" )
ax2.set_xlabel( "age of father")
ax2.set_ylabel( "# paternal DNMs")
ax2.scatter(merged["Father_age"], merged["paternal_dnm"])
fig.savefig( "Ex2_b.png" )
#plt.show()

# PART 2.2---------------------------------------------------------------------------------------------------------------------------------------

mama_model = smf.ols(formula = "maternal_dnm ~ 1 + Mother_age", data = merged)
results = mama_model.fit()
print(results.summary())


# PART 2.3---------------------------------------------------------------------------------------------------------------------------------------

papa_model = smf.ols(formula = "paternal_dnm ~ 1 + Father_age", data = merged)
results = papa_model.fit()
print(results.summary())


# PART 2.4---------------------------------------------------------------------------------------------------------------------------------------

new = pd.DataFrame({"Father_age" : [50.5]})
#print(new)    

papa_model = smf.ols(formula = "paternal_dnm ~ 1 + Father_age", data = merged).fit()
print(papa_model.predict(new))

# PART 2.5---------------------------------------------------------------------------------------------------------------------------------------

fig, ax3 = plt.subplots()
ax3.set_title( "Maternal vs Paternal DNMs" )
ax3.set_xlabel( "# DNMs")
ax3.set_ylabel( "Frequency")
ax3.hist(merged["maternal_dnm"], label = "maternal", bins = 30, alpha = 0.5)
ax3.hist(merged["paternal_dnm"], label = "paternal", bins = 30, alpha = 0.5)
ax3.legend()
fig.savefig( "Ex2_c.png" )
#plt.show()

# PART 2.6----------------------------------------------------------------------------------------------------------------------------------------

import scipy.stats as sps

print(sps.ttest_ind(merged["maternal_dnm"], merged["paternal_dnm"]))

