#Problem Link :- https://leetcode.com/problems/n-th-tribonacci-number/
#Code 
"""
Very similar to the one for regular fibonnaci numbers
    Populate an array with the three base numbers in the sequence.
    Then, if n = 0, 1, or 2, return directly
    Otherwise, build the array to the nth Tribonacci number, and return.
"""

#!/bin/python
import math
import os
import re
import sys

def tribonacci( n):
    DP = [0,1,1]
    if n < 3:
        return DP[n]
    for i in range(3,n+1):
        r = DP[i-1]+DP[i-2]+DP[i-3]
        DP.append(r)
    return DP[n]
    
if __name__ == '__main__':

    n = input()
    print tribonacci(n)


#Time Complexity : O(N)