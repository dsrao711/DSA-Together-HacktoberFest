
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/


# Approach without using stacks : 'Strings/Easy/super_reduced_string.py'


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        for i in s :
            
            if (stack):
                
                top = stack.pop()
                stack.append(top)
                
                if(top == i):
                    stack.pop()
                else:
                    stack.append(i)    
            else:
                stack.append(i)
        
        return "".join(stack)