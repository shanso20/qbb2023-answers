import sys

fname = sys.argv[1]
data = open(fname).readlines()

# print(data) to check that correct file was imported

def my_mean(list_name):
	sum_list = sum(list_name)
	average = sum_list/len(list_name)
	return average

numbers = []
for x in data:
	x = x.rstrip("\n")
	x = int(x)
	numbers.append(x)
# print(numbers) to check that a list of integers was created

print(my_mean(numbers))