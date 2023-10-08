#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here

    dictionary = {}

    sorted_array = sorted(arr)

    for x in sorted_array:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1

    maxValue = -1
    maxKey = None

    for key, value in dictionary.items():
        if value > maxValue:
            maxValue = value
            maxKey = key

    return maxKey


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
