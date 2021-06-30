
#https://practice.geeksforgeeks.org/problems/ncr1019/1#

class Solution:
    def nCr(self, n, r):
        # code here
        #Pascals triangle
        if(r>n):
            return 0
            
        if(n == r):
            return 1
            
        if(n-r < r):
            r = n-r
            
        mod = 10000000007  
        dp = [0]*(r+1)
        dp[0] = 1
        
        for i in range(1 , n+1):
            j = min(i , r)
            while(j > 0):
                dp[j] = ((dp[j-1] % mod) + (dp[j] % mod) ) % mod 
                j -= 1
                
        return dp[r]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends