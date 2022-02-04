# Question : https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Video ref : https://youtu.be/w36ekZYq-Ms

import bisect

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        n = len(matrix)
        # Low 
        l = matrix[0][0]
        # High
        h = matrix[n-1][n-1]
        # kth element is somewhere between 1st and last element in the mat since it is sorted
        while(l < h):
            m = (l + h) / 2
            # count = Number of elements less than mid
            count = 0 
            # Count the elements less than mid for each row
            for i in range(0 , n):
                count += bisect.bisect_right(matrix[i], m)
            # If count is less than k , low has to be modified else high will be modified
            if(count < k):
                l = m + 1
            else:
                h = m
        # Once l == h , loop breaks and l is kth smallest element 
        return l
        
# TC : O(n) + O(nlogn)
# SC : O(1)
