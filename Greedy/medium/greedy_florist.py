#Problem Link :- https://www.hackerrank.com/challenges/greedy-florist/problem
#Code 
"""
The strategy is to use the first few times to buy the most expensive flowers, and buy the least expensive flowers the last. 
To do this, we will need to sort the cost to descending order, and start buying flowers from the start of the list
"""

#!/bin/python

import math
import os
import re
import sys

def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    previous_purchase = 0
    for i in range(n):
        cost += (previous_purchase +1) * c[i]
        if (i+1)%k==0:
            previous_purchase += 1
    return cost
    
if __name__ == '__main__':

    nk = raw_input().split()
    n = int(nk[0])
    k = int(nk[1])

    c = map(int, raw_input().rstrip().split())

    minimumCost = getMinimumCost(k, c)
    print str(minimumCost)



#Time Complexity : O(N)