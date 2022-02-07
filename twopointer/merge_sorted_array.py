# https://leetcode.com/problems/merge-sorted-array/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # pointer 1 = m - 1
        # pointer 2 = n - 1
        last = m + n - 1
        # Since both arrays are sorted , check if last ele of nums2 is greater than nums1 
        # If yes, then nums2's last ele will be the last ele of nums1
        # Else , it means that nums1's last non zero ele is the largest ele possible so it goes to last 
        # Decreament the pointers and last accordingly
        while(m and n):
            if(nums1[m-1] < nums2[n-1]):
                nums1[last] = nums2[n-1]
                n -= 1
            else:
                nums1[last] = nums1[m-1]
                m -= 1
                
            last -= 1
        # If any elements are left in nums2 , append them in nums1     
        while(n):
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1