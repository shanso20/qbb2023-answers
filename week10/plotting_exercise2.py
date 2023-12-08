#!/usr/bin/env python

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

oldpeople = pd.read_csv("centenarians.csv", index_col = 0)

ages = oldpeople["age"]
gender = oldpeople["gender"]

women = []
men = []

for i, j in enumerate(ages):
	if gender.iloc[i] == "female":
		women.append(j)
	elif gender.iloc[i] == "male":
		men.append(j)

fig, ax = plt.subplots()
ax.violinplot([women, men])
ax.set_title("Oldest People Ever")
ax.set_xticks([1, 2], labels = ["women", "men"])
ax.set_ylabel("Age")
fig.savefig("Exercise2-2-1.png")

# PLOT 2 -------------------------------------------------------------------------------------------------------------------

deathplace = oldpeople["place_of_death_or_residence"]

countries = {}
for i in deathplace:
	if i not in countries and "France" not in i:
		countries[i] = 1
	elif "France" in i and "France" not in countries:
		countries["France"] = 1
	elif "France" in i and "France" in countries:
		countries["France"] += 1
	else:
		countries[i] += 1

xlabels = list(countries.keys())
ylabels = list(countries.values())

fig1, ax1 = plt.subplots()
ax1.bar(xlabels, ylabels)
ax1.set_title("Deathplaces/ Residencies of Oldest People")
ax1.set_xlabel("Country")
ax1.set_ylabel("Number of Oldest People")
plt.xticks(rotation = 90)
plt.tight_layout()
fig1.savefig("Exercise2-2-2.png")

# PLOT 3 ---------------------------------------------------------------------------------------------------------------------------------------------

birthdates = oldpeople["birth_date"]

year = []
for i in birthdates:
	x = i[0:4]
	x = int(x)
	year.append(x)

fig2, ax2 = plt.subplots()
ax2.hist(year)
ax2.set_title("Birthyears of Oldest People on Record")
ax2.set_xlabel("Year of Birth")
ax2.set_ylabel("Number of People")
fig2.savefig("Exercise2-2-3.png")