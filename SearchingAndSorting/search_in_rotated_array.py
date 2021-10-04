# Leetcode - 33
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        op = -1
        for i in range(0 , len(nums)):
          if (nums[i] == target):
            op = i
        return op
          