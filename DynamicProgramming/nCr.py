
#https://practice.geeksforgeeks.org/problems/ncr1019/1#

#Tabulation method
class Solution:
    def nCr(self, n, r):
        # code here
        dp = [[0 for x in range(r+1)] for x in range(n+1)]
        mod = 10**9 + 7
        for i in range(n+1):
            for j in range(min(i , r)+1):
                if(j == i or j == 0):
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-1])%mod
        
        return dp[n][r] 
    

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