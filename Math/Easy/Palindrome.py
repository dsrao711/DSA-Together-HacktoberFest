#Link to prob:https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:# function to check if plaindrome
        a=0
        revx=x
        if(x<0):#for negative numbers as -121 is not equal to 121-
            return False
        while x != 0:# loop to reverse number
            digit = x % 10
            a = a * 10 + digit
            x //= 10
        if(a == revx):# to check if its plaindrome
            return True
        else:
            return False


#TIme complexity: O(logN)        
