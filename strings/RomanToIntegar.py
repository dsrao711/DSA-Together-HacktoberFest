# Link : https://leetcode.com/problems/roman-to-integer/submissions/

# Approach :

# 1. 

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
          "I" : 1 , "V"  :5 , "X" : 10 , "L" : 50 , "C" : 100 , 
          "D" : 500 , "M" : 1000
        }
        
        res = 0
        n = len(s)
        
        for i in range(1 , n):
          
          if(values[s[i-1]] < values[s[i]] ):
            res -= values[s[i-1]]
          else:
            res += values[s[i-1]]
            
        res += values[s[len(s) - 1]]
        return res
            
            