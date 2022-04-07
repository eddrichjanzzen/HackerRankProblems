#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    
    highScore = -1
    lowScore = sys.maxsize
    highScoreCount = 0
    lowScoreCount = 0
    
    for s in scores: 
        if (s > highScore):
            highScore = s
            highScoreCount+=1
        
        if (s < lowScore):
            lowScore = s
            lowScoreCount+=1
            
    return [highScoreCount-1, lowScoreCount-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()