#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Get dataset to recreate Fig 3B from Lott et al 2011 PLoS Biology https://pubmed.gov/21346796
# wget https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/bulk_RNA-seq/extra_data/all_annotated.csv

f = open("/Users/cmdb/Desktop/swc-python/Day_2_Lecture/all_annotated.csv", "r")
data = f.readlines()
#-------------------------------------------------------------------------------------

transcripts = []
for x in data[1:]:
    x = x.rstrip("\n")
    x = x.split(",")
    x = x[0]
    transcripts.append(x)
#print(transcripts[0])
# Don't look at anything below this; I loaded just the transcripts here, saved in the list transcripts. Below, I did the same for the samples and the data.

#---------------------------------------------------------------------------------------
samples_2 = []
samples = data[0]
for x in samples:
    x = samples.rstrip("\n")
    x = x.split(",")
samples_2.append(x)
# print(transcripts_2)

samples_3 = samples_2[0]
# print(transcripts_3)

samples_4 = samples_3[2:]
#print(samples_4)

#---------------------------------------------------------------------------------------------------------

data_2 = []
for x in data[1:]:
    x = x.rstrip("\n")
    x = x.split(",")
    x = x[2:]
    #print(x)


#transcripts = np.loadtxt( "/Users/cmdb/Desktop/swc-python/Day_2_Lecture/all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
 # print( "transcripts: ", transcripts[0:5] )

#samples = np.loadtxt( "/Users/cmdb/Desktop/swc-python/Day_2_Lecture/all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
# print( "samples: ", samples[0:5] )

#data = np.loadtxt( "/Users/cmdb/Desktop/swc-python/Day_2_Lecture/all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
#print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
#for i in range(len(transcripts)):
#   if transcripts[i] == 'FBtr0073461':
#        row = i

# Find columns with samples of interest
cols_females = []
cols_males = []
for i in range(len(samples_4)):
    if "female" in samples_4[i]:
        cols_females.append(i)
    else:
        cols_males.append(i)
# print(cols_females)
# print(cols_males)


# Subset data of interest
F_expression = data_2[row, cols_females]
M_expression = data_2[row, cols_males]

# Prepare data
x_females = samples_4[cols_females]
x_males = samples_4[cols_males]
y_females = F_expression
y_males = M_expression

y_males_2 = 2 * y_males

x_axis = []
for x in range(len(x_males)):
    x_axis.append(x_males[x].lstrip("male_"))
# print(x_axis)

# Plot data
fig, ax = plt.subplots()
ax.set_title( "sisA" )
ax.set_xlabel( "developmental stage")
ax.set_ylabel( "mRNA abundance (RPKM)")
ax.plot( x_axis, y_males )
ax.plot( x_axis, y_females )
ax.plot( x_axis, y_males_2 )
fig.savefig( "FBtr0073461.png" )
plt.close( fig )