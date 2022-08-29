# Link : https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1


##Complete this function
def maxSubArraySum(a,size):
    ##Your code here
    
   max_current = a[0]
   max_global = max_current
   for i in range (1 , size):
       max_current = max(max_current + a[i] , a[i])
       max_global = max(max_current , max_global)
   return max_global
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends