#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows) :
        triangle = [[1]*i for i in range(1,numRows+1)]
        
        i = 1
        
        while(i < numRows):
          
          j = 1
          
          for j in range(1 ,len(triangle[i-1])):
            
            triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
                         
          i += 1
          
        return triangle