# Leetcode - 33
# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag = 0
        for i in range(0 , len(nums)):
          if (nums[i] == target):
            op = i
            flag = 1
        if (flag == 0):
          op = -1
        return op
          