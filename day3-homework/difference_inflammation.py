#!/usr/bilbn/env python
import sys

fname = sys.argv[1]
data = open(fname).readlines()

def patient_difference(patient_index_a, patient_index_b):

	integers = []
	for x in data:
		x = x.rstrip("\n")
		x = x.split(",")

	# print(x) will give a list of lists, each containing the values as strings and with the extra return removed
		numbers = []
		for y in x:
			y = int(y)
			numbers.append(y)
		integers.append(numbers)

	patient_A = integers[patient_index_a]
	patient_B = integers[patient_index_b]

	differences = []

	for day in range(len(patient_A)):
		difference = patient_A[day] - patient_B[day]
		differences.append(difference)

	return differences

print(patient_difference(4, 5))


#patient_A[1] - patient_B[1]

# for day in patient_A:
# 	for same_day in patient_B:
# 		same_day = day - same_day
# 	differences.append(same_day)
#print(differences)
