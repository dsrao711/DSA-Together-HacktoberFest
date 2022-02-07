# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        l, r = 0, x
        ans = 0
        while l < r:
            mid = (l+r)//2
            if mid*mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid
                
        return ans