#Problem Link :- https://leetcode.com/problems/new-21-game/
#Code

#!/bin/python

import math
import os
import re
import sys

def new21Game(N, K, W):
    idp = [0.0] * (K+W)
    #First, the probability of 1.0 is dealt with
    #That is, I fall in [K, min (n, K + W-1)]
    for i in range(K, min(N, K+W-1) + 1):
        dp[i] = 1.0
        
    #Here we first calculate the case of K - 1
    #The derived formula is put here
    dp[K-1] = float(min(N-K+1, W) / W)
    #Here we start to calculate the value of DP [0] from K-2
    for i in range(K-2, -1, -1):
        dp[i] = dp[i+1] - (dp[i+W+1]-dp[i+1]) / W
    return dp[0]
    
if __name__ == '__main__':

    nk = raw_input().split()
    n = int(nk[0])
    k = int(nk[1])
    p = int(nk[2])

    print new21Game(n,k,p)



#Time Complexity : O(N)