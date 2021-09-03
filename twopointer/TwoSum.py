# https://leetcode.com/problems/two-sum/submissions/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hashmap = {}
        arr = []
        
        for i in range(0,n):
            if target-nums[i] in hashmap:
                arr.append(hashmap[target-nums[i]])
                arr.append(i)
                return arr
            
            else:
                hashmap[nums[i]] = i