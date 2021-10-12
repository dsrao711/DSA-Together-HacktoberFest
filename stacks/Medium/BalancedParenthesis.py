# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, x):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for char in x :
            if (char in ["(" , "{" , "["]):
                
                stack.append(char)
                
            else:
                
                if not stack:
                    return False
                    
                current_char = stack.pop()
                
                if current_char == "(" :
                    if char != ")":
                        return False
                        
                if current_char == "[" :
                    if char != "]":
                        return False
                        
                if current_char == "{":
                    if char != "}":
                        return False
                        
        if stack :
            return False
            
        return True