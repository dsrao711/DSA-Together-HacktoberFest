
# Problem : https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/submissions/

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count=0
        for j,i in enumerate(s1):
            if i not in s2:
                return False
            if s1[j]!=s2[j]:
                count+=1
        if count==2 or count==0:
            return True
        return False
    
    
# Steps : 

# Condition : 1) Return true if : To get the strings with same charachters but the arrangement should be same with one swap allowed
#                                  i.e Two chars can be at different position but rest of the chars should be at the same position
#             2)Return true if  : If strings are exactly equal


# Compare every element of both the string and increment the counter if elements do not match 
# If the count == 0 or count == 2 -> return true


# Enumerate :
# j -> index no of the string 
# i -> char of the string
