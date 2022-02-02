#https://leetcode.com/problems/trapping-rain-water/submissions/ 

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if not height:
            return 0
        
        n = len(height)
        left_pointer = 0 
        right_pointer = n - 1
        res = 0
        
        left_max = height[left_pointer]
        right_max = height[right_pointer]
        
        while(left_pointer < right_pointer):
            if(left_max < right_max) : 
                left_pointer += 1
                left_max = max(height[left_pointer] , left_max)
                res += (left_max - height[left_pointer])
            else:
                right_pointer -= 1
                right_max = max(height[right_pointer] , right_max)
                res += (right_max - height[right_pointer] )
                
        return res
                
        
        
        