#https://leetcode.com/problems/subarray-sum-equals-k/submissions/

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        d = {0:1}
        n = len(nums)
        s = 0
        
        for i in range(0 , n):
          s += nums[i]
          if(s-k in d):
            count += d[s-k]
            
          if (s in d):
            d[s] += 1
          else:
            d[s] = 1
            
        return count
    
    
# Time complexity : O(n). The entire numsnums array is traversed only once.

# Space complexity : O(n). Hashmap can contain up to n distinct entries in the worst case.