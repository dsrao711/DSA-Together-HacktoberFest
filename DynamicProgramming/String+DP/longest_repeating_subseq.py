# https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1#
class Solution:
    def LongestRepeatingSubsequence(self, s):
        # Code here
        n = len(s)
        a = s
        b = s
        dp = [[0 for i in range(n+1)]for j in range(n+1)]
        for i in range(1 , n+1):
            for j in range(1 , n+1):
                if(i == 0 or j == 0):
                    dp[i][j] = 0
                if((a[i-1] == b[j-1] )and i!= j):
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        return dp[n][n]


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.LongestRepeatingSubsequence(str)
        print(ans)
