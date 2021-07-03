

class Solution:
    def MissingNumber(self,a,N):
        # code here

        total = (N)*(N+1)/2
        total_a = sum(a)
        return int(total - total_a)
        

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