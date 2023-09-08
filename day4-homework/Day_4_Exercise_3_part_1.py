#!/usr/bilbn/env python

import numpy as np
import matplotlib.pyplot as plt

def my_mean(list_name):
	sum_list = sum(list_name)
	average = sum_list/len(list_name)
	return average

def genetic_drift(allele_freq, pop_size):

	AF = []

	while 0 < allele_freq < 1:
		allele_freq = np.random.binomial(2 * pop_size, allele_freq)/ (2 * pop_size)
		AF.append(allele_freq)

	return AF

# trial_1 = genetic_drift(0.5, 1754)
# print(len(trial_1))


# allele_freq = 0.5
population = [50, 100, 150, 200, 250]

averages = []
for pop in population:

	fixation_time = []
	for i in range(50):
		trials = genetic_drift(0.5, pop)
		fixation_time.append(trials)

#print(fixation_time)
#print(len(fixation_time))

	fixation_length = []
	for x in fixation_time:
		fixation_length.append(len(x))

	
	average_fixation = my_mean(fixation_length)
	#print(average_fixation)
	averages.append(average_fixation)
print(averages)

fig, ax = plt.subplots()

ax.scatter(population, averages)

ax.set_title( "Exercise 3" )
ax.set_xlabel( "Population Size")
ax.set_ylabel( "Time to Fixation")

fig.savefig( "Day_4_Exercise_3_part_1" )
plt.show()

