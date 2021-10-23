#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
	for i in range(n):
		for j in range(n):
			if j != ((n -1) - i):
				print(' ', end='')
			else:
				x = '#' * (i+1)
				print(x , end='')
		print()

if __name__ == '__main__':
	n = int(input().strip())

	staircase(n)
