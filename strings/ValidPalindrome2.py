# Link : https://leetcode.com/problems/valid-palindrome-ii/submissions/

# Two pointer approach
# TC : O(n)

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Use two pointers at the start and end of the string 
        # To iterate over the string from the left
        a_pointer = 0 
        # To iterate over the string from the right
        b_pointer = len(s) - 1
        
        while(a_pointer <= b_pointer):
          # Condition for palindrome is that the charachters must be same when read reverse
          # Find the index where the charachters dont match for a_pointer and b_pointer
          if(s[a_pointer] != s[b_pointer]):
            # Skip the index where the charachters dont match 
            s1 = s[ : a_pointer] + s[a_pointer + 1 : ]
            s2 = s[ : b_pointer] + s[b_pointer + 1 : ]
            # Return True if the string is a palindrome after removing one charachter , else false
            return (s1 == s1[ : :-1] or s2 == s2[ : :-1])
        
          # Towards right
          a_pointer += 1
          # Towards left
          b_pointer -= 1
          
        return True
            
            