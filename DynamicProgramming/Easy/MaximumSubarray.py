# Link : https://leetcode.com/problems/maximum-subarray/

# DP approach 

# Refer Kadanes algo solution in Arrays

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dp approach 
        
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        
        for i in range(1 , len(nums)):
          if(nums[i] < nums[i] + dp[i-1]):
            dp[i] = nums[i] + dp[i-1]
          else:
            dp[i] = nums[i]
            
        return max(dp)