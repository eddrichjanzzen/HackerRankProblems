#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here

    searched = []
    count = 0

    for a in range(0, len(ar)):
        tempCount = 1
        current = ar[a]
                
        if current not in searched:
            searched.append(current)
        else:
            continue
        for b in ar[a+1:]:
            next = b
            if current == next:
                tempCount+=1
            
        print(tempCount // 2)
        count += (tempCount // 2)
    
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()