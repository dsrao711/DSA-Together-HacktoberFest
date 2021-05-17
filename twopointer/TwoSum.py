


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        
        while start != end:
            sum = nums[start] + nums[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]

        
        