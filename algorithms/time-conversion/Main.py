#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

import re
 
# Function to remove all leading
# zeros from a a given string
def removeLeadingZeros(str):
 
    # Regex to remove leading
    # zeros from a string
    regex = "^0+(?!$)"
 
    # Replaces the matched
    # value with given string
    str = re.sub(regex, "", str)

    return str

def timeConversion(s):
    
    time = s.split(':')
    hours = int(removeLeadingZeros(time[0]))
    time[2] = time[2][0:2]
    
    if s.endswith('PM'):
      if hours != 12:
        time[0] = str(hours + 12)

    elif s.endswith('AM') and hours == 12:
      time[0] = str('00')

    return ":".join(time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    # s = '12:45:54PM'

    result = timeConversion(s)

    print(result)

    fptr.write(result + '\n')

    fptr.close()
