#!/usr/bin/env python
import sys

bait_info = []
for line in open("h19_chr20and21.baitmap"):
	fields = line.rstrip('\n').split("\t")
	bait_info.append(fields)
output_info_1 = []
for line in open("output_washU_text.txt"):
	fields = line.rstrip('\n').split("\t")
	temp = []
	for i in fields:
		if i.startswith("chr"):
			i = i.split(",")
			temp.append(i)
		else:
			temp.append(i)
	temp_2 = [temp[0][0], temp[0][1], temp[0][2], temp[1][0], temp[1][1], temp[1][2], temp[2]]
	output_info_1.append(temp_2)

output_info_2 = []
scores = []
for i in output_info_1:
	scores.append(float(i[-1]))
for i in output_info_1:
	score = int((float(i[-1])/max(scores)) * 1000)
	i.append(score)
	if int(i[1]) < int(i[4]):
		i.append(i[0])
		i.append(i[1])
		i.append(i[3])
		i.append(i[5])
	else:
		i.append(i[3])
		i.append(i[4])
		i.append(i[0])
		i.append(i[2])
	output_info_2.append(i)

bait = []
bait_pos = []
output_info_3 = []
for i in bait_info:
	bait.append([i[1], i[-1]])
for i in output_info_2:
	for x in range(len(bait)):
		if bait[x][0] != i[1]:
			continue
		else:
			bait_pos.append([i[0], i[1], i[2]])
			i.append(bait[x][1])
	output_info_3.append(i)

output_info = []
output_info_4 = []
for i in output_info_3:
	for x in range(len(bait)):
		if bait[x][0] == i[4]:
			i.append(bait[x][1])
			i.append("+")
	output_info_4.append(i)
for i in output_info_4:
	if i[-1] != "+":
		i.append(".")
		i.append("-")
	output_info.append(i)

baittobait = []
baittotarg = []
for i in output_info:
	if i[-1] == "+":
		baittobait.append(i)
	else:
		baittotarg.append(i)
top_baittobait = []
top_baittotarg = []
for i in baittobait:
	if 970 <= i[7] <= 1000:
		top_baittobait.append(i)
for i in baittotarg:
	if 740 <= i[7] <= 1000:
		top_baittotarg.append(i)

line_1 = []
for i in output_info:
	line_1.append([i[0], i[-6], i[-4], ".", i[-8], i[-9], ".", "0", i[0], i[1], i[2], i[-3], "+", i[3], i[4], i[5], i[-2], i[-1]])

fp = open("week8_ucsc.bed", "w")
line = []
for i in line_1:
	i = str(i)
	i = i.rstrip("]").lstrip("[")
	i = i.replace("'", "")
	i = i.replace(", ", "	")
	i = i.replace(" ", "	")
	line.append(i)
	fp.write(i+"\n")
fp.close()
