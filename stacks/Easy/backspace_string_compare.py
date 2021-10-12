# Link : https://leetcode.com/problems/backspace-string-compare/

# Stack approach

# Iterate through the string and push elements in a stack after checking if the element is a "#"
# If the element is a "#" , pop the top ele of the stack
# If not , simply push the ele into the stack 
# Convert the stack into a string

# Do this process for both s and t 
# Return true if the o/p strings of s and t are equal

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build(S):
        
          stack = []

          for i in S : 
            # IF a "#" is encountered , a backspace has to be performed 
            if i != "#":
              stack.append(i)
            elif stack : 
              # Backspace
              stack.pop()
              
          return "".join(stack)
        
        # Check if both strings are same after applying backspaces
        return build(s) == build(t)
            
        
# Complexity Analysis

# Time Complexity: O(M + N)O(M+N), where M, NM,N are the lengths of S and T respectively.

# Space Complexity: O(M + N)

