# Link to Problem : https://leetcode.com/problems/counting-bits/


# Naive Approach 1 : Using Math  and inbuilt python function 
# 1. Convert Int to Bin
# 2. Count 1's in the Binary String
# 3. Append the 1's in o/p array ans

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        
        for i in range(0 , n + 1):
            
          binary = format(i , "b")
          ones = str(binary).count('1')
          ans.append(ones)
          
        return ans
          
          
# Dynamic Programming approach 

class Solution:
    def countBits(self, n) :
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            if(i % 2 == 0):
                result[i] = result[i // 2]  
            else: 
                result[i] = result[i // 2] + 1
        return result
