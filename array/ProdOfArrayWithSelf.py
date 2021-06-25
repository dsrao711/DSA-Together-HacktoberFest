
#https://leetcode.com/problems/product-of-array-except-self/submissions/

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left_arr = [1]*n
        right_arr = [1]*n
        op = []
        
        
        for i in range(1 , n):
        
          left_arr[i] = left_arr[i-1]*nums[i-1]
          right_arr[n-i-1] = right_arr[n-i]*nums[n-i]
          
        
        for j in range(0 ,n):
          op.append(left_arr[j]*right_arr[j])
          
        return op