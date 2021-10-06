#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1/

class Solution:
    def MissingNumber(self,array,n):
        ans = 0 
        for i in range(n-1):
            ans^=array[i]
            ans^=(i+1)
        ans^=n
        return ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends
