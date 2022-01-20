# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for digi in digits:
            res=res*10+digi
        res+=1
        res = list(str(res))
        return res
    
    
# 