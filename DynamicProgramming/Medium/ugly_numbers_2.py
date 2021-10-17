#https://leetcode.com/problems/ugly-number-ii/

# Condition for ugly number -> Multiple of either 2/3/5

# 2^p2 3^p3 5^p5

# p2,p3,p5 are powers for 2 , 3 ,5

class Solution:
    def nthUglyNumber(self, n: int) -> int:
      
        dp = [1] + [0] * (n-1)
        
        # Initialize 3 pointers for 2,3,5
        
        p2 = p3 = p5 = 0
        for i in range(1, n):
            
            # Next ugly number will be minimum of these three 
        
            dp[i] = min (dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            
            #If the number is a multiple of 2 , increase the power of 2 
            
            if dp[i] == dp[p2] * 2: p2 += 1
            if dp[i] == dp[p3] * 3: p3 += 1
            if dp[i] == dp[p5] * 5: p5 += 1
              
             
        return dp[-1]
    
    