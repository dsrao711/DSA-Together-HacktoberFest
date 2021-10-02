#https://practice.geeksforgeeks.org/problems/count-squares3649/1#

class Solution:
    def countSquares(self, N):
        # code here 
        return int((N - 1)**0.5)

import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
