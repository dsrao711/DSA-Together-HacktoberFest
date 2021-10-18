#Link to the problem : https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        
        #sign is used to store whether the number is positve or negative
        sign = 1
        if x<0 :
            sign = -1
            x = -x  #x is now always positive
        
        rev = 0; #reverae number
        
        #rev is the absolute reverse number
        #rev*sign is the signed reverse number
        #dividing x until it becomes 0
        while x:
            rev = rev*10 + x%10 
            x //=10
            
            #condition answer(rev) should not go outside the signed 32-bit integer range
            if rev*sign >= 2**31 or rev*sign < -2**31:
                return 0  #returning 0 if outside the range
        
        return rev*sign  #final ans

#Auxiliary Space: O(1)
#Time Complexity: O(logn) base 10