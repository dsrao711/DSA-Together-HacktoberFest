# Leetcode : https://leetcode.com/problems/3sum/submissions/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        # Set to avoid repitition
        op = set()
        # Impossible in this case
        if(n < 3):
            return op
        nums.sort()
        for i in range(n - 2):   
            if(i != 0 and nums[i] == nums[i - 1]):
                continue 
            # Target = Original target - nums[i] 
            # Target = 0 - nums[i]
            target = - nums[i]  
            lo = i + 1
            hi = n - 1
            while(lo < hi):
                # Pair sum whose total is equal to the new target
                pair = nums[lo] + nums[hi]
                if(pair == target) :
                    op.add((nums[lo] , nums[hi] , nums[i]))
                if(pair < target):
                    lo += 1
                else:
                    hi -= 1
                    
        return list(op)[::-1]
                    
                    
            
                
            