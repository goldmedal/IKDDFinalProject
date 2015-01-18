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
	sorted(suit_table[i])
	sorted(rank_table[i])
	sorted(hand_table[i])

#rank_table2 = rank_table
#print rank_table2[0:10]
#result_table = np.zeros([2,2,3,4,2,2,2,2,4,13,13,13,13,13,11])
#for i in range(0, num):
for i in range(0, 5):
	aaa = list(suit_table[i])
	aaa.extend([1])
	print aaa
	#print list(suit_table[i]).append([1,1,1])
	hand = list(suit_table[i]).extend(rank_table[i])
	second = hand
	print hand
	hand.extend(hand_table[i])
	first = hand
	print second
	print first

	#result_table[suit_table[i,0], suit_table[i,1], suit_table[i,2], suit_table[i,3]-2, rank_table[i,8], rank_table[i,9], rank_table[i,10], \
	#			 rank_table[i,11]-1, rank_table[i,12]-1, hand_table[0], hand_table[1], hand_table[2], hand_table[3], hand_table[4], data[i,10]]
	#result_table[suit_table[i,0], suit_table[i,1], suit_table[i,2], suit_table[i,3]-2, rank_table2[i,8], rank_table2[i,9], rank_table2[i,10], \
	#			 rank_table[i,11]-1, rank_table[i,12]-1, hand_table[0], hand_table[1], hand_table[2], hand_table[3], hand_table[4], 10]



#for i in range(0, 10):
	#print num_table[i]
	#print card_table[i]
			
#for i in xrange(number_of_classes):
#	for j in xrange(number_of_price_brackets):
#		for k in range(0, 2):
			
#			women_only_stats = data[ (data[0::,4] == "female") \
#                                 & (data[0::,5].astype(np.float) == k) \
#  	                              & (data[0::,2].astype(np.float) == i+1) \
#                                 & (data[0:,9].astype(np.float) >= j*fare_bracket_size) \
#                                 & (data[0:,9].astype(np.float) < (j+1)*fare_bracket_size), 1]

#			men_only_stats = data[ (data[0::,4] != "female") \
#                                 & (data[0::,5].astype(np.float) == k) \
#                                 & (data[0::,2].astype(np.float) == i+1) \
#                                 & (data[0:,9].astype(np.float) >= j*fare_bracket_size) \
#                                 & (data[0:,9].astype(np.float) < (j+1)*fare_bracket_size), 1]
#
#			if np.size(women_only_stats.astype(np.float)) != 0:	
#				survival_table[0,k,i,j] = np.mean(women_only_stats.astype(np.float))  # Female stats
#			if np.size(men_only_stats.astype(np.float)) != 0:
#				survival_table[1,k,i,j] = np.mean(men_only_stats.astype(np.float))    # Male stats

#survival_table[ survival_table < 0.5 ] = 0
#survival_table[ survival_table >= 0.5 ] = 1
