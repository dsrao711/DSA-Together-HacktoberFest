class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for i in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n - 1 and j == m - 1:
                    dp[i][j] = grid[i][j]
                elif i == n - 1:
                    dp[i][j] = dp[i][j + 1] + grid[i][j]
                elif j == m - 1:
                    dp[i][j] = dp[i + 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        return dp[0][0]