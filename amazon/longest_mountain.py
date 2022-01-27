# My approach 
# https://leetcode.com/problems/longest-mountain-in-array/

class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        max_mountain  = 0
        
        dp_left = [0]*n 
        for i in range(1 , n ):
            if(arr[i-1] < arr[i]):
                dp_left[i] = dp_left[i-1] + 1 
        print(dp_left)    
        
        dp_right = [0]*n
        for i in range(n-2 , -1 , -1):
            if(arr[i+1] < arr[i]):
                dp_right[i] = dp_right[i+1] + 1
        print(dp_right)    
        
        for i in range(0 , n):
            if(dp_right[i] > 0 and dp_left[i] > 0 ) :
                mountain = dp_right[i] + dp_left[i] + 1
                max_mountain = max(max_mountain , mountain)
                
        return max_mountain
            