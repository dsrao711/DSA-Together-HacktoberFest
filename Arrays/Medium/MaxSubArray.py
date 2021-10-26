# https://leetcode.com/problems/maximum-subarray/

# Using Kadanes Algorithm - Approach 1 

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxCurrent = maxGlobal = nums[0]
        if (len(nums) == 1):
          maxGlobal = nums[0]
        elif(len(nums) == 0):
          maxGlobal = -1
        else:
          for i in range(1 , len(nums)):
            maxCurrent = max( nums[i]+maxCurrent , nums[i])

            if(maxCurrent > maxGlobal):
              maxGlobal = maxCurrent
            
        return maxGlobal