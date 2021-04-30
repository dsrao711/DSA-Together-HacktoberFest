   
# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1
   
class Solution :
   
    def majorityElement(self, A, N):
        #Your code here
        occ = {}
        flag = 0
        for i in A :
            if i in occ :
                occ[i] += 1
            else:
                occ[i] = 1
        count = 0
        for key in occ :
            if(occ[key] > N/2):
                flag = 1
                count = key
                break
            
        if (flag == 0):
            count = -1
            
        return count
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends