#https://leetcode.com/problems/delete-and-earn/

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = [0]*(max(nums) + 1)
        
        # Store the freq of each ele in counter
        for i in nums :
            counter[i] += i
            
        #House robber problem 
        
        n = len(counter)
        
        if (n == 1):
            return nums[0]
        
        if (n <= 2):
            return max(nums)
        
        dp = [0]*n
        
        dp[0] = counter[0]
        dp[1] = max(counter[0] , counter[1])
        
        for i in range(2 , n):
            dp[i] = max(dp[i-2] + counter[i] , dp[i-1])
            
        return dp[-1]
        
        
        
        
        