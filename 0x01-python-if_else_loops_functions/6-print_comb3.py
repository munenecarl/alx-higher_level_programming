#!/usr/bin/python3

# run iterations from 0 to 99
# print the iteration number
# 

for i in range(0, 10):
	for j in range(i + 1, 10):
		if i == 8 and j == 9:
			print("{:d}{:d}".format(i, j))
		else:
			print("{:d}{:d}, ".format(i, j), end="")
			