# Hackerrank : https://www.hackerrank.com/challenges/reduced-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    i = 0
    while i < len(s)-1 :
      if(s[i] == s[i+1]):
        s = s[:i] + s[i+2:]
        i = 0
      else:
        i += 1
      
    if(len(s) != 0) :
      return s
    else:
      return 'Empty String'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
