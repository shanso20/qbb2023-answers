#!/usr/bilbn/env python
import sys

fname = sys.argv[1]
data = open(fname).readlines()

#print(data) #to check that file was imported

def my_mean(list_name):
	sum_list = sum(list_name)
	average = sum_list/len(list_name)
	return average

def patient_average(patient_index):

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

# print(integers) to check that you now have a list of lists containing integers
# need to select one patient whose inflammation values I will average.

# print(integers[4]) to check that I can select just the values for patient 5
	answer = my_mean(integers[patient_index])
	return answer

print(patient_average(4))
