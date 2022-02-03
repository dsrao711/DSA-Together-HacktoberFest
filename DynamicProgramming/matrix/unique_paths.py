#https://leetcode.com/problems/unique-paths/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0]*n for i in range(m)]        
        
        for i in range(m-1 , -1 , -1):
            for j in range(n-1 , -1 , -1):
                if(i == m-1):
                    # Bottom most - only right possible
                    dp[i][j] = 1
                if(j == n-1):
                    # Right most - only bottom possible
                    dp[i][j] = 1
                if (i < m - 1 and j < n - 1):
                    # Any other ele = paths through right + paths through bottom
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                    
        return dp[0][0]
                    
                
                    
                
        