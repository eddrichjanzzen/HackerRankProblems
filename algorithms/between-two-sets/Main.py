#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
from math import gcd

def lcm(a, b): 
    return (a * b) // gcd(a, b)
        
def gcd_list(arr):
    return reduce(gcd, arr)

def lcm_list(arr):
    return reduce(lcm, arr)

def evenly_divides(num, divisor): 
    return (num % divisor) == 0
    
    
def getTotalX(a, b):
    lcm_value = lcm_list(a)
    
    gcd_value = gcd_list(b)
    
    counter = 0
    
    multiple_of_lcm = lcm_value
    while multiple_of_lcm <= gcd_value:
        if evenly_divides(gcd_value, multiple_of_lcm):
            counter += 1
        multiple_of_lcm += lcm_value
        
    return counter
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
