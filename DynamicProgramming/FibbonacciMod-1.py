# Approach 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#
from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacciModified(t1, t2, n):
    # Write your code here
    
    if(n==2):
      return t2
    else:
      return fibonacciModified(t2 , t1 + t2**2 , n-1)
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
