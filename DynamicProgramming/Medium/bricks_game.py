#Problem Link :- https://www.hackerrank.com/challenges/play-game/problem
#Code 

"""
The ideas behind this approach is this :
> At any step, no matter the player, he will always make the optimal move
> We do a bottom up approach, meaning we start from the end of the array and calculate the optimal move at that step (ex: if we have only 1 brick left what is the optimal move? what if we have 2 , what if 3, etc . . .)

The variables used :
> rev_arr: contains the reversed array; we reverse the array to start from the bottom and go all the way to the top
> process: contains the optimal move calculated at every step
> sum_arr: the cumulative sum of the elements in the array

The steps :
> for the first 3 steps since we have a maximum of 3 bricks the optimal move is to pick all the bricks we have so we calculate the value of the picked bricks and we store it in the process array
> from the 3rd step : have 3 cases : pick one, two or three bricks. No matter the number of bricks we pick we are sure that the next move made by the second player will be the optimal move of the remaining and that value is stored in the process array. so we know the value of our pick and the value of the next move
"""

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