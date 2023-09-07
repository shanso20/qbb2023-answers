#!/usr/bilbn/env python

my_list = [1, 2, 3, 4, 5]

def my_mean(list_name):
	sum_list = sum(list_name)
	average = sum_list/len(my_list)
	return average
	
print(my_mean(my_list))
