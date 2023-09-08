#!/usr/bilbn/env python

import numpy as np
import matplotlib.pyplot as plt

def genetic_drift(allele_freq, pop_size):

	AF = []

	while 0 < allele_freq < 1:
		allele_freq = np.random.binomial(2 * pop_size, allele_freq)/ (2 * pop_size)
		AF.append(allele_freq)

	return AF

# trial_1 = genetic_drift(0.5, 1754)
# print(len(trial_1))


fig, (ax1, ax2) = plt.subplots(2)

for i in range(30):
	trials = genetic_drift(0.5, 1754)
	x_positions = range(len(trials))
	y_positions = trials
	ax1.plot(x_positions, y_positions)


ax1.set_title( "Genetic Drift" )
ax1.set_xlabel( "Number of Generations")
ax1.set_ylabel( "Allele Frequency")
fig.savefig( "Genetic_Drift_Day_4_Exercise_1" )


hist_x = []
for i in range(1000):
	trials = genetic_drift(0.5, 1754)
	x_positions = len(trials)
	hist_x.append(x_positions)



ax2.hist(hist_x)

ax2.set_title( "Allele Fixation" )
ax2.set_xlabel( "Time to Fixation")
ax2.set_ylabel( "Distribution")
plt.tight_layout()
fig.savefig( "Day_4_Exercise_2" )
plt.show()

# Get a starting frequency and a population size
# These are the input parameters for the function

# Make a list to store allele frequencies called AF

# While our allele frequency is between 0 and 1:
	# Get the new allele frequency for next generation by drawing from the binomial distribution. But this doesnt give you frequency, just number of successes
	# Convert number of successes into a frequency

	# Store our allele frequency in teh AF list


# Return a list of the allele frequency at each time point
# Number of generation to fixation is the length of this list

