# Problem  : https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums, target):
      
      # First sort the array
      nums = sorted(nums)

      # A set to store the quadruplets
      quadruplets = set()

      # Store the length of 'nums' to 'lenNums'
      lenNums = len(nums)

      # Initialize values
      i = 0
      j = i+1

      # Traverse till the 4th last element
      while i < lenNums-3:
        # print(i)
        j = i+1
        # For each value of 'i' traverse from i+1 to the 3rd last element
        while j < lenNums-2:
          # For each pair value of 'i' & 'j', take two pointers at j+1 and at lenNums-1
          low = j+1
          high = lenNums-1
          # Traverse until 'low' is less than 'high'
          while low < high:
            # Store the sum of the quadruplets
            fourSum = nums[i] + nums[j] + nums[low] + nums[high]
            # IF the summed value is equal to 'target'
            if fourSum == target:
              # Then add the quadruplet to the list
              quadruplets.add(tuple(sorted([nums[i], nums[j], nums[low], nums[high]])))

              # Check for duplicates and increase 'low'
              while low < high and nums[low] == nums[low+1]:
                low += 1

              # Check for duplicates and decrease 'high'
              while high > low and nums[high] == nums[high-1]:
                high -= 1

              # Change both the values of 'low' & 'high'
              low += 1
              high -= 1
            # ELSE IF the summed value is greater then 'target', decrease 'high'
            elif fourSum > target:
              high -= 1
            # ELSE, increase 'low'
            else:
              low += 1
          # END while
          # Check for duplicates
          while j < lenNums-2 and nums[j] == nums[j+1]:
            j += 1
          j += 1
        # END while
        # Check for duplicates
        while i < lenNums-3 and nums[i] == nums[i+1]:
          i += 1
        i += 1
      # END while

      return quadruplets