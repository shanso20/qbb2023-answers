#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Get dataset to recreate Fig 3B from Lott et al 2011 PLoS Biology https://pubmed.gov/21346796
# wget https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/bulk_RNA-seq/extra_data/all_annotated.csv

transcripts = np.loadtxt( "/Users/cmdb/Desktop/swc-python/Day_2_Lecture/all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
 # print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "/Users/cmdb/Desktop/swc-python/Day_2_Lecture/all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
# print( "samples: ", samples[0:5] )

data = np.loadtxt( "/Users/cmdb/Desktop/swc-python/Day_2_Lecture/all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
# print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i

# Find columns with samples of interest
cols_females = []
cols_males = []
for i in range(len(samples)):
    if "female" in samples[i]:
        cols_females.append(i)
    else:
        cols_males.append(i)
# print(cols_females)
# print(cols_males)


# Subset data of interest
F_expression = data[row, cols_females]
M_expression = data[row, cols_males]

# Prepare data
x_females = samples[cols_females]
x_males = samples[cols_males]
y_females = F_expression
y_males = M_expression

x_axis = []
for x in range(len(x_males)):
    x_axis.append(x_males[x].lstrip("male_"))
print(x_axis)

# Plot data
fig, ax = plt.subplots()
ax.set_title( "FBtr0073461" )
ax.plot( x_axis, y_males )
ax.plot( x_axis, y_females )
fig.savefig( "FBtr0073461.png" )
plt.close( fig )