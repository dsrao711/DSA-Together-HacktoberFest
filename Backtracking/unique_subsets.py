class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        def backtracking(i , subsets):
            if(i >= len(nums)):
                res.append(subsets.copy())
                return
            # All subsets that include nums[i]
            subsets.append(nums[i])
            backtracking(i+1 , subsets)
            subsets.pop()
            # ALl subsets that dont include nums[i]
            while(i+1 < len(nums) and nums[i] == nums[i+1]):
                i += 1
            backtracking(i+1 , subsets)
            
        backtracking(0 , [])
        
        return res