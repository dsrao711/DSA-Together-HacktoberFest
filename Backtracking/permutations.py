"""
Link - https://leetcode.com/problems/permutations

Difficulty - Medium

Big-O:

Time: O(N*N!)
Space: O(N!)
"""

def recursive(nums, perm=[], res=[]):
        
            if not nums: 
                res.append(perm) # --- no need to copy as we are not popping/backtracking. Instead we're passing a new variable each time 

            for i in range(len(nums)): 
                newNums = nums[:i] + nums[i+1:]
                # perm.append(nums[i]) # --- instead of appending to the same variable
                newPerm = perm + [nums[i]] # --- new copy of the data/variable
                recursive(newNums, newPerm, res) 
                # perm.pop()  # --- no need to backtrack
            return res
        
        return recursive(nums)