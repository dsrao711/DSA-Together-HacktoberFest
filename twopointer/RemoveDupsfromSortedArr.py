# Remove Duplicates from Sorted Array

# Link to problem : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Its clearly stated in the question that a new space cannot be allocated

class Solution:
    def removeDuplicates(self, nums):
      i = 0
      while i < len(nums) - 1 :
        if nums[i] == nums[i+1]:
          del nums[i]
        else:
          i += 1
      return len(nums)
  
  