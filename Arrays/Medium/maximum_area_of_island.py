# Link : https://leetcode.com/problems/max-area-of-island/

# Approach :
# We are supposed to return the maximum area formed by ones but satisfying this condition 
# The ones should be connected to each other either horizontally / vertically , not diagonally 
# Eg : 
# [0 1 0 
#  1 1 1
#  0 1 0] 


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))