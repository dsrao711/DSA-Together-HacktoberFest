# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        
        """
        :type height: List[int]
        :rtype: int
        """
        
        n = len(height)
        max_area = 0
        # Left pointer
        l = 0 
        # right pointer
        r = n - 1
        
        while(l < r):
            area = (min(height[l] , height[r])) * (r - l)
            max_area = max(max_area , area)
            if(height[l] < height[r]):
                l += 1
            else:
                r -= 1
        
        return max_area