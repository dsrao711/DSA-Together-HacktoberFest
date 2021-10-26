#Problem Link :- https://www.hackerrank.com/challenges/play-game/problem
#Code 
#!/bin/python

import math
import os
import re
import sys


def bricksGame(arr):
    rev_arr = arr[::-1]
    process = [0 for i in range(len(arr))]
    sum_arr = [0 for i in range(len(arr))]

    for i in range(len(rev_arr)):
        
        if i == 0:
            sum_arr[0] = rev_arr[i]
        else:
            sum_arr[i] = sum_arr[i-1] + rev_arr[i]

        if i < 3:
            process[i] = sum(rev_arr[:i+1])
        else: 
            case1 = rev_arr[i] + (sum_arr[i-1] - process[i-1])
            case2 = sum(rev_arr[i-1:i+1]) + (sum_arr[i-2] - process[i-2])
            case3 = sum(rev_arr[i-2:i+1]) + (sum_arr[i-3] - process[i-3])

            process[i] = max(case1, case2, case3)

    return process[-1]


if __name__ == '__main__':
 
    t = int(raw_input().strip())

    for t_itr in xrange(t):
        arr_count = int(raw_input().strip())

        arr = map(int, raw_input().rstrip().split())

        result = bricksGame(arr)
        print str(result)


#Time Complexity : O(N)