#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    n = len(h)
    max_area = 0
    
    for i in range(0 , n):
      
      left_index = i-1
      right_index = i + 1
      count = 1
      while(left_index >= 0):
        if(h[left_index] >= h[i]):
          count += 1
          left_index -= 1
        else:
          break
          
          
      while(right_index < n):
        if(h[right_index] >= h[i]):
          count += 1
          right_index += 1
        else:
          break
      
      max_area = max(max_area , count*h[i])
        
    
    return max_area
        
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
