#https://leetcode.com/problems/smallest-range-ii/submissions/

class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        if(len(nums) == 1):
          return 0
        else:
          score = nums[-1] - nums[0]
          for i in range(0 , len(nums)-1):
            nums_max = max(nums[i]+k , nums[-1]-k)
            nums_min = min(nums[i+1]-k , nums[0]+k)
            score = min(score , nums_max - nums_min)
            
        return score
