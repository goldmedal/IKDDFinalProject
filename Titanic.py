"""
Author : RLai

"""

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb'))       # Load in the csv file
header = csv_file_object.next()                             # Skip the fist line as it is a header
data=[]                                                     # Create a variable to hold the data

num = 0
for row in csv_file_object:                 # Skip through each row in the csv file
	data.append(row)                        # adding each row to the data variable
	num = num + 1
data = np.array(data)                       # Then convert from a list to an array

print num
suit_table = np.zeros([num, 4])
rank_table = np.zeros([num, 13])
hand_table = np.zeros([num, 5])
#survival_table = np.zeros([2,2,number_of_classes,number_of_price_brackets],float)

for i in range(0, num):
	for j in range(0, 5):
		suit_table[i, int(data[i, j*2])-1] += 1
		rank_table[i, int(data[i, j*2+1])-1] += 1
		hand_table[i, j] = int(data[i, j*2+1])-1
	#sorted(suit_table[i])
	#sorted(rank_table[i])
	#sorted(hand_table[i])

#rank_table2 = rank_table
#print rank_table2[0:10]
#result_table = np.zeros([2,2,3,4,2,2,2,2,4,13,13,13,13,13,11])
result_table1 = []
result_table2 = []
for i in range(0, num):
	if i == 15000:
		print 123
#for i in range(0, 5):
	#hand = list(suit_table[i]).extend(rank_table[i])
	suit_table.sort()
	hand = list(suit_table[i])
	rank_table.sort()
	hand.extend(rank_table[i,8:])
	second = list(hand)
	#print hand
	hand_table.sort()
	hand.extend(hand_table[i])
	first = hand
	#print second
	#print first

	index = 0
	for item in result_table1:
		if item[0] == first:
			index = 1
	
	if index == 0:
		result_table1.append([first, int(data[i, 10])])
	
	index = 0

	for item in result_table2:
		if item[0] == second:
			index = 1

	if index == 0:
		result_table2.append([second, int(data[i, 10])])


