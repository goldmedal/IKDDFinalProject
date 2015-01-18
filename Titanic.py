"""
Author : RLai

"""

import csv as csv
import numpy as np

def test(data, first_table, second_table):
	suit_table = np.zeros(4)
	rank_table = np.zeros(13)
	hand_table = np.zeros(5)

	for i in range(0,5):
		suit_table[int(data[i*2])-1] += 1
		rank_table[int(data[i*2+1])-1] += 1
		hand_table[i] = int(data[i*2+1]) - 1

	suit_table = list(sorted(suit_table))
	rank_table = sorted(rank_table)
	rank_table = rank_table[8:]
	hand_table = sorted(hand_table)
	suit_table.extend(rank_table)
	second_result = list(suit_table)
	suit_table.extend(hand_table)
	first_result = suit_table

	ans = -1
	check = 0
	for item in first_table:
		if item[0] == first_result :
			ans =  item[1]
			check = 1
			break

	if check > 1 :
		for item in second_table :
			if item[0] == second_result :
					ind = item[1].max()
					ans = item[1].index(ind)
				break

	print ans

	return

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

for i in range(0, num):
	for j in range(0, 5):
		suit_table[i, int(data[i, j*2])-1] += 1
		rank_table[i, int(data[i, j*2+1])-1] += 1
		hand_table[i, j] = int(data[i, j*2+1])-1

result_table1 = []
result_table2 = []
for i in range(0, num):
	suit_table.sort()
	hand = list(suit_table[i])
	rank_table.sort()
	hand.extend(rank_table[i,8:])
	second = list(hand)
	hand_table.sort()
	hand.extend(hand_table[i])
	first = hand

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


data = ['1','9','2','1','2','2','4','4','2','8']
test(data,result_table1,result_table2)
