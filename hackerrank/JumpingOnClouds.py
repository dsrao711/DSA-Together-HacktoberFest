#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    n = len(c)
    i = 0
    if(n == 1):
      return 0
    while(i<n):
      if(i+2 < n and c[i+2] == 0):
        jumps += 1
        i += 2
      elif(i+1 < n and c[i+1] == 0):
        jumps += 1
        i += 1
      else:
        i += 1
        
    return jumps
    
    
    
        
    return jumps
      
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
