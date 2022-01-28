#https://leetcode.com/problems/longest-increasing-subsequence/
#https://www.youtube.com/watch?v=odrfUCS9sQk

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        # for first ele , longest sub seq is the number itself
        dp[0] = 1
        
        for i in range(1,n):
            # Longest sub seq length possible for current ele nums[i]
            max_for_i = 0
            # For every element in nums , check if the elements before it are less than the curr
            # ele so that it forms a increasing sub-seq
            for j in range(0 , i):
                # Of all the elements to the right of current ele nums[i] which are less than nums[i] , 
                # store the subseq with the max length in the dp 
                if(nums[j] < nums[i]):
                    if(dp[j] > max_for_i):
                        # Update the max for current element
                        max_for_i = dp[j]
            # Include the curr element in the sub seq     
            dp[i] = max_for_i + 1
            
        print(dp)
        # from the dp array , find the max length and return the answer
        longest_inc_sub_seq = 1
        for i in range(0 , n):
            if(dp[i] > longest_inc_sub_seq):
                longest_inc_sub_seq = dp[i]
                
        return longest_inc_sub_seq
        