# https://leetcode.com/problems/maximum-product-subarray/submissions/

"""
For cases like : [2,3,4] => Product is always going to increase since all nums are +ve
For cases like : [-2 , -3 , -4] => Product is always going to decrease since all nums are -ve
For cases like : [-2 , 3 , 4] =>  Product may increase or decrease bcoz of the sign 

If we use one variable to store the max , we may end up getting a value lesser than expected due
to encountering of negative numbers and zeroes in between 

So we use two variables to store the max and min product respectively 

curr_max = max(nums[i] , curr_max * nums[i] , curr_min * nums[i])
curr_min = min(nums[i] , curr_max * nums[i] , curr_min * nums[i])

Note : For curr_min , we dont require the updated curr_max , hence to avoid the updated curr_max being 
used , we store curr_max*nums[i] in a variable temp 

temp = curr_max * nums[i]

So ,

curr_min = min(nums[i] , temp , curr_min * nums[i])

res = max(res , curr_max)

Dry run for 1st sample input:

For nums = [2,3,-2,4]

curr_max = 1
curr_min = 1
res = max([2,3,-2,4]) = 4

1. i = 0 

curr_max = max(2 , 2*1 , 2*1) = 2
curr_min = min(2 , 2*1 , 2*1) = 2
res = 4

2. i = 1

curr_max = max(3 , 3*2 , 3*2) = 6
curr_min = min(3 , 3*2 , 3*2) = 3
res = 6

3. i = 2

curr_max = max(-2 , -2*6 , -2*3) = -2
curr_min = min(-2 , -2*6 , -2*3) = -12
res = 6

4. i = 3

curr_max = max(4 , 4*-2 , 4*-12) = 4
curr_min = min(4 , 4*-2 , 4*-12) = -48
res = 6


o/p : res = 6


"""

class Solution(object):
    def maxProduct(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr_max = 1
        curr_min = 1
        res = max(nums)
        
        for i in range(0 , len(nums)):
            
            if(nums[i] == 0):
                # Avoid zeroes
                curr_max = 1 
                curr_min = 1
                continue
                
            # Computing temp to store the curr_max * nums[i] , so as to avoid using the                 updated value of curr_max while calculating curr_min
            temp = curr_max * nums[i]
            
            curr_max = max(curr_max * nums[i] , curr_min * nums[i] , nums[i])
            curr_min = min(temp , curr_min * nums[i] , nums[i])
            
            res = max(res , curr_max)
            
        return res
    
"""
TC : O(n)

"""
        
    
        
        