
#https://leetcode.com/problems/squares-of-a-sorted-array/submissions/

class Solution:
    def sortedSquares(self, nums):
        for i in range(0 , len(nums)):
          nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums