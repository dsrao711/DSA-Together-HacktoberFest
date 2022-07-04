
# Link : https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1/?page=5&curated[]=1&sortBy=submissions#
# Video : https://youtu.be/HrybPYpOvz0

class Solution:
    def longestCommonSubstr(self, X, Y, m, n):
        dp = [[0 for k in range(n+1)] for l in range(m+1)]
        # To store the length of
        # longest common substring
        lcss = 0
        # TD approach
        for i in range(m + 1):
            for j in range(n + 1):
                if (i == 0 or j == 0):
                    dp[i][j] = 0
                elif (X[i-1] == Y[j-1]):
                    dp[i][j] = dp[i-1][j-1] + 1
                    lcss = max(lcss, dp[i][j])
                else:
                    dp[i][j] = 0
        return lcss

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
