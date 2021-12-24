# Problem link : https://github.com/xizhengszhang/Leetcode_company_frequency
# TC : O(k)

"""
We are expected to return max sum obtained by using k cards either from left or right
We use the sliding window approach to define a window of size = n - k 
and remaining elements in the array excluding the window elements are considered to be the
current sum 
We keep on moving the window till the right pointer reaches the end and calculate the current sum
The max of all the curr_sum is the output

"""

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        # Left pointer and right pointer for defining the window
        l = 0 
        r = len(cardPoints) - k
        curr_sum = sum(cardPoints[r:])
        max_sum = curr_sum
        
        while(r < len(cardPoints)):
            curr_sum += (cardPoints[l] - cardPoints[r])
            max_sum = max(curr_sum , max_sum)
            l += 1
            r += 1
        
        return max_sum
        
        