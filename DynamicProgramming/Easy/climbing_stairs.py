
# https://leetcode.com/problems/climbing-stairs/submissions/

# Bottom Up approach 

class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):
          return 1
        dp = [0]*(n)
        dp[0] = 1
        dp[1] = 2
        for i in range(2 , n):
          dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
        
        
# Memoization

from functools import lru_cache

class Solution:
    @lru_cache(maxsize = 1000)
    def climbStairs(self, n: int) -> int:
        if(n == 0 or n == 1):
          return 1
        else:
          return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        