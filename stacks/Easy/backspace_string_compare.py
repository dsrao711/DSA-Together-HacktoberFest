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

# Two Pointer Approach
# In this approach idea is to keep track of '#' characters in the string. If we iterate from
# right to left in a given string, for each character encountered we have 2 possible scenarios:
# If character is '#', then we know in advance that we have to ignore next alphabetical character if present.
# This can be done by storing count of '#' characters seen till this index.
# If character is lowercase alphabet, then again 2 scenarios are there:
# If we have non-zero count of '#' character, then this means we can safely ignore this character
# Else this character will be included in current string.
# For 2 strings we keep moving their specific index pointers (from right to left) until
# either both strings are traversed till leftmost index (means matching strings)
# or one of them becomes empty ( means non matching strings)
# or both reach an index consisting of lowercase characters . In this case :
# if characters are same we continue the same process as above.
# if not same , simply return false.

class TwoPointerSolution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # we start from rightmost end of both strings
        s_pointer = len(s) - 1
        t_pointer = len(t) - 1

        # keep track of backspace symbols seen till now
        s_backspace_count = 0
        t_backspace_count = 0

        # process both strings until all symbols are seen
        while s_pointer >= 0 or t_pointer >= 0:

            # keep shifting s_pointer until we have some backspace symbols left or current character is backspace
            while s_pointer >= 0 and (s_backspace_count or s[s_pointer] == '#'):
                s_backspace_count += 1 if s[s_pointer] == '#' else -1
                s_pointer -= 1

            # keep shifting t_pointer until we have some backspace symbols left or current character is backspace
            while t_pointer >= 0 and (t_backspace_count or t[t_pointer] == '#'):
                t_backspace_count += 1 if t[t_pointer] == '#' else -1
                t_pointer -= 1

            # if we finally reach some indices with lowercase alphabet present at both indices of s and t respectively
            if s_pointer >= 0 and t_pointer >= 0 and (s[s_pointer] != t[t_pointer]):
                return False

            # if in one string we are at some lowercase character and other string is already exhausted and vice-versa
            if (s_pointer >=0 and t_pointer < 0) or (s_pointer < 0 and t_pointer >= 0):
                return False

            # decrement current index in s if it's non-negative
            if s_pointer > -1:
                s_pointer -= 1

            # decrement current index in t if it's non-negative
            if t_pointer > -1:
                t_pointer -= 1

        # we reach here only when both strings are matching
        return True


# Complexity Analysis

# Time Complexity: O(M + N), where M, NM,N are the lengths of S and T respectively.

# Space Complexity: O(1)
