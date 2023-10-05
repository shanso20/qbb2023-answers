#!/usr/bilbn/env python

from fasta import readFASTA
import numpy as np
import sys
import pandas as pd
#from Bio import pairwise2


# EXERCISE 1 -----------------------------------------------------------------------------------------------------------------------------------------------------------


def global_alignment(fasta_sequences_file, scoring_matrix_file, gap_penalty, alignment_filepath):

	input_sequences = readFASTA(open(fasta_sequences_file))

	seq1_id, sequence1 = input_sequences[0]
	seq2_id, sequence2 = input_sequences[1]


	#print(input_sequences[0])

	scoring_matrix = pd.read_csv(scoring_matrix_file, delim_whitespace=True)

	F_matrix = np.zeros((len(sequence1) + 1, len(sequence2) + 1))
	Trackeback = np.zeros((len(sequence1) + 1, len(sequence2) + 1))

	for i in range(len(sequence1) + 1):
		F_matrix[i, 0] = i * gap_penalty
		Trackeback[i, 0] = 1

	for j in range(len(sequence2) + 1):
		F_matrix[0, j] = j * gap_penalty
		Trackeback[0, j] = -1


	for i in range(1, F_matrix.shape[0]):
		for j in range(1, F_matrix.shape[1]):
			d = F_matrix[i-1, j-1] + scoring_matrix.loc[sequence1[i-1], sequence2[j-1]]
			h = F_matrix[i, j-1] + gap_penalty
			v = F_matrix[i-1, j] + gap_penalty

			max_val = max(d, h, v)

			F_matrix[i,j] = max_val

			if d == max_val: 
				Trackeback[i,j] = 0
			elif h == max_val:
				Trackeback[i,j] = -1
			else:
				Trackeback[i, j] = 1

	sequence_1_alignment = ""
	sequence_2_alignment = ""

	i = len(sequence1)
	j = len(sequence2)
	cell = Trackeback[i, j] #starting point at bottom right hand corner of matrix
	#print(sequence1[i-1])
	print(fasta_sequences_file)
	print("Alignment score: ", F_matrix[i, j]) #alignment score

	while i > 0 or j > 0:
		if cell == 0:
			sequence_1_alignment = sequence_1_alignment + sequence1[i-1]
			sequence_2_alignment = sequence_2_alignment + sequence2[j-1]
			i -= 1
			j -= 1
		elif cell == -1:
			sequence_1_alignment = sequence_1_alignment + "-"
			sequence_2_alignment = sequence_2_alignment + sequence2[j-1]
			j -= 1
		else:
			sequence_1_alignment = sequence_1_alignment + sequence1[i-1]
			sequence_2_alignment = sequence_2_alignment + "-"
			i += -1
		cell = Trackeback[i, j]

	sequence_1_alignment = sequence_1_alignment[::-1]
	sequence_2_alignment = sequence_2_alignment[::-1]

	#print(sequence_1_alignment)
	#print(len(sequence_1_alignment))
	#print(len(sequence1))

	#print(sequence_2_alignment)
	#print(len(sequence_2_alignment))
	#print(len(sequence2))


	output = open(alignment_filepath, "w")
	output.write("sequence 1 alignment")
	output.write('\n')
	#output.write(str(Trackeback))
	output.write(sequence_1_alignment + '\n')
	output.write("sequence 2 alignment")
	output.write('\n')
	output.write(sequence_2_alignment + '\n')
	output.close()
	# print(F_matrix, file = output)
	#print(Trackeback)

	gap_list_1 = []
	gap_list_2 = []

	for space in sequence_1_alignment:
		if space == "-":
			gap_list_1.append("-")
	#print(gap_list_1)
	print("Number of gaps in sequnece 1: ", len(gap_list_1))

	for space in sequence_2_alignment:
		if space == "-":
			gap_list_2.append("-")
	#print(gap_list_2)
	print("Number of gaps in sequence 2: ", len(gap_list_2))

	#print(pairwise2.align.globalxx(sequence_1_alignment, sequence_2_alignment))

global_alignment("CTCF_38_M27_AA.faa", "BLOSUM62.txt", -10, "aa_alignment_file")
print(global_alignment)

global_alignment("CTCF_38_M27_DNA.fna", "HOXD70.txt", -300, "dna_alignment_file")
print(global_alignment)
# goals:
# print # gaps in first sequence, # gaps in second sequence, score of final alignment

# run script twice: 
#		first, fasta_sequences_file = CTCF DNA transcript, scoring_matrix_file = HOXD70, gap_penalty = -300
#		next, fasta_sequences_file = CTCF amino acid sequences from human vs mouse, scoring_matrix_file = BLOSUM62, gap_penalty = -10