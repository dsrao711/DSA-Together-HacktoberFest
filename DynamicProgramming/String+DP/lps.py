# 
class Solution:
    def longestCommonSubsequence(self, x: str, y: str) -> int:
        m=len(x)
        n=len(y)
        dp=[[-1]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
        
                elif x[i-1] == y[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                        
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
                        
        return dp[m][n]
    
    def longestPalindromeSubseq(self, s: str) -> int:
        rev_s = s[::-1]
        lps = self.longestCommonSubsequence(s , rev_s)
        return lps