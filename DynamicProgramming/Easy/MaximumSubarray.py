# Link : https://leetcode.com/problems/maximum-subarray/

# DP approach 

# Refer Kadanes algo solution in Arrays


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """
            The idea of this approach is to traverse the array linearly and update the array such that arr[i] holds the
            maximum sum of all the sub arrays ending at index i.

            While traversing when we are at index k (k>0), arr[k-1] contains the maximum sum of all the sub arrays ending at index k-1.
            So if arr[k-1] is positive we will update arr[k] as arr[k] = arr[k] + arr[k-1].
            otherwise , we will not do anything because the array [arr[k]] is the sub array which gives maximum sum of all
            the sub arrays ending at index k.

            Time complexity :- O(n) because we are linearly traversing the array once.
            Space complexity :- O(1) because we are not using any extra space.

        """

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]

        return max(nums)

