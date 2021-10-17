# https://leetcode.com/problems/house-robber/



class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        # Base case
        if (n == 1):
            return nums[0]
        
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])
        
        for i in range(2 , n):
            # Max of (best decision for not adjacent house + current house) and (best decision for previous house)
            dp[i] = max(dp[i-2] + nums[i] , dp[i-1])
            
        return dp[-1]