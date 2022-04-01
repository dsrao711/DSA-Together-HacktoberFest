
class Solution:
    def count(self, S, m, n): 
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(0 , m):
            for j in range(S[i] , n + 1):
                dp[j] += dp[j - S[i]]
        return dp[n]

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
