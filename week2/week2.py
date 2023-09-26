#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats 


# EXERCISE 1-----------------------------------------------------------------------------------------------------------------------------------------

def simulate_coverage(coverage, genome_len, read_len, figname):

	coverage_arr = np.zeros(genome_len)
	
	num_reads = int(coverage * genome_len / read_len)

	low = 0
	high = genome_len - read_len 

	start_positions = np.random.randint(low=0, high=high + 1, size=num_reads) # high is exclusive

	for start in start_positions:
		coverage_arr[start: start+read_len] += 1

	x = np.arange(0, max(coverage_arr)+1)

	sim_0cov = genome_len - np.count_nonzero(coverage_arr)
	sim_0cov_pct = 100* sim_0cov / genome_len

	print(f'In the simulation, there are {sim_0cov} bases with 0 coverage')
	print(f'This is {sim_0cov_pct}% of the genome')

	# Get poisson distribution
	# lambda = mu = coverage = 3
	y_poisson = stats.poisson.pmf(x ,mu=coverage) * genome_len

	# Get normal distribution
	# mean = loc = coverage
	# scale = stdev = 1.73 = sqrt(3) = sqrt(coverage)
	y_normal = stats.norm.pdf(x, loc=coverage, scale=np.sqrt(coverage)) * genome_len

	fig, ax = plt.subplots()
	ax.hist(coverage_arr, bins=x, align='left', label='Simulation')
	ax.plot(x, y_poisson, label='Poisson')
	ax.plot(x, y_normal, label='Normal')
	ax.set_xlabel('Coverage')
	ax.set_ylabel('Frequency (bp)')
	ax.legend()
	fig.tight_layout()
	fig.savefig(figname)


simulate_coverage(3, 1000000, 100, 'Ex1_3x_cov.png')

# Ex.1.4-------------------------------------------------------------------------------------------------------------------------------------------------------------

def simulate_coverage(coverage, genome_len, read_len, figname):

	coverage_arr = np.zeros(genome_len)
	
	num_reads = int(coverage * genome_len / read_len)

	low = 0
	high = genome_len - read_len 

	start_positions = np.random.randint(low=0, high=high + 1, size=num_reads) # high is exclusive

	for start in start_positions:
		coverage_arr[start: start+read_len] += 1

	x = np.arange(0, max(coverage_arr)+1)

	sim_0cov = genome_len - np.count_nonzero(coverage_arr)
	sim_0cov_pct = 100* sim_0cov / genome_len

	print(f'In the simulation, there are {sim_0cov} bases with 0 coverage')
	print(f'This is {sim_0cov_pct}% of the genome')

	# Get poisson distribution
	# lambda = mu = coverage = 10
	y_poisson = stats.poisson.pmf(x ,mu=coverage) * genome_len
	print(stats.poisson.pmf(k=0, mu=10) * genome_len)

	# Get normal distribution
	# mean = loc = coverage
	# scale = stdev = sqrt(10) = sqrt(coverage)
	y_normal = stats.norm.pdf(x, loc=coverage, scale=np.sqrt(coverage)) * genome_len
	print(stats.norm.pdf(0, loc = 10))


	fig, ax = plt.subplots()
	ax.hist(coverage_arr, bins=x, align='left', label='Simulation')
	ax.plot(x, y_poisson, label='Poisson')
	ax.plot(x, y_normal, label='Normal')
	ax.set_xlabel('Coverage')
	ax.set_ylabel('Frequency (bp)')
	ax.legend()
	fig.tight_layout()
	fig.savefig(figname)


simulate_coverage(10, 1000000, 100, 'Ex1_10x_cov.png')

# Ex. 1.5--------------------------------------------------------------------------------------------------------------------------------------------------------------

def simulate_coverage(coverage, genome_len, read_len, figname):

	coverage_arr = np.zeros(genome_len)
	
	num_reads = int(coverage * genome_len / read_len)

	low = 0
	high = genome_len - read_len 

	start_positions = np.random.randint(low=0, high=high + 1, size=num_reads) # high is exclusive

	for start in start_positions:
		coverage_arr[start: start+read_len] += 1

	x = np.arange(0, max(coverage_arr)+1)

	sim_0cov = genome_len - np.count_nonzero(coverage_arr)
	sim_0cov_pct = 100* sim_0cov / genome_len

	print(f'In the simulation, there are {sim_0cov} bases with 0 coverage')
	print(f'This is {sim_0cov_pct}% of the genome')

	# Get poisson distribution
	# lambda = mu = coverage = 30
	y_poisson = stats.poisson.pmf(x ,mu=coverage) * genome_len
	print(stats.poisson.pmf(k=0, mu=30) * genome_len)

	# Get normal distribution
	# mean = loc = coverage
	# scale = stdev = sqrt(30) = sqrt(coverage)
	y_normal = stats.norm.pdf(x, loc=coverage, scale=np.sqrt(coverage)) * genome_len
	print(stats.norm.pdf(0, loc = 30))

	fig, ax = plt.subplots()
	ax.hist(coverage_arr, bins=x, align='left', label='Simulation')
	ax.plot(x, y_poisson, label='Poisson')
	ax.plot(x, y_normal, label='Normal')
	ax.set_xlabel('Coverage')
	ax.set_ylabel('Frequency (bp)')
	ax.legend()
	fig.tight_layout()
	fig.savefig(figname)


simulate_coverage(30, 1000000, 100, 'Ex1_30x_cov.png')


# EXERCISE 2----------------------------------------------------------------------------------------------------------------------------------------------------------

graph = set()


reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

k = 3

for read in reads:
	for i in range(len(read)-k):
		#len(read)-k = 5 - 3 = 2, so range(2) = i = 0, 1

		kmer1 = read[i: i + k]
		# kmer1 = read[0:3], read[1:4]
		# gives a list of kmers of length 3, 2 per read--letters 1-3 and letters 2-4

		kmer2 = read[i + 1: i + 1 + k]
		# kmer2 = read[1: 4], read[2: 5]
		# gives a list of kmers of length 3, 2 per read--letters 2-4 and letters 3-5

		# add "kmer1 --> kmer2" to graph
		graph.add((kmer1, kmer2))
#print(graph)


for edge in graph:
	print(edge)

# Ex. 2.2------------------------------------------------------------------------------------------------------------------------------------------------------------

# in command line:
# conda create -n graphviz -c conda-forge graphviz
# conda activate graphviz

# Ex. 2.3-----------------------------------------------------------------------------------------------------------------------------------------------------------

output = open("test.dot", "w")
#print(graph, file = output)


print("digraph graphfile {", file = output)

for edge in graph:
	kmer1, kmer2 = edge
	print(f"{kmer1} -> {kmer2};", file = output)

print("}", file = output)
	
	#kmer1 -> kmer2;

output.close()

# Ex. 2.4-----------------------------------------------------------------------------------------------------------------------------------------------------------

# in command line:
# dot -Tpng -oex2_digraph.png test.dot




