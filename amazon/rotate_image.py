class Solution(object):
      
    def transpose(self , matrix ):
      n = len(matrix)
      for i in range(n):
        for j in range(i , n):
          matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
          
    def reflect(self , matrix):
      n = len(matrix)
      for i in range(0 , n):
        for j in range( n//2):
          matrix[i][j] , matrix[i][-j-1] = matrix[i][-j-1] , matrix[i][j]
          
    def rotate(self, matrix):
      
        """
        
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place             instead.
        
        """
    
        self.transpose(matrix)
        self.reflect(matrix)
        
        
        
            
            