# https://leetcode.com/problems/set-matrix-zeroes/

# With extra space
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        rows_set = set()
        cols_set = set()
        
        for i in range(0 , r):
            for j in range(0 , c):
                if(matrix[i][j] == 0):
                    rows_set.add(i)
                    cols_set.add(j)
                    
        for i in range(r):
            for j in range(c):
                if(i in rows_set or j in cols_set):
                    matrix[i][j] = 0
                    
        return matrix
                
# Without extra space
class Solution(object):
    def setZeroes(self, matrix):
        
        r = len(matrix)
        c = len(matrix[0])
        
       # set these variables if any 0th col or 0th row ele is 0
    
        is_col_0 = False
        is_row_0 = False
        
       # 1. check if any element in 0th row is 0 
        
        for j in range(0 , c):
            if(matrix[0][j] == 0):
                is_row_0 = True
        
       # 2. check if any element in 0th col is 0
    
        for i in range(0 , r):
            if(matrix[i][0] == 0):
                is_col_0 = True
        
       # 3.  update 0th index of row and 0th index of col on encountering 0s
        
        for i in range(1 , r):
            for j in range(1 , c):
                if(matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
    
       # 4 . Set entire row 0 on checking 0 in 0th col
        
        for i in range(1 , r):
            if(matrix[i][0] == 0):
                for j in range(0 , c):
                    matrix[i][j] = 0
            
       # 5.  Set entire col 0 on checking 0 in 0th row
    
        for j in range(1 , c):
            if(matrix[0][j] == 0):
                for i in range(0 , r):
                    matrix[i][j] = 0
                    
       # 6.  Set entire 0th col 0 if is_col_0 true
    
        if(is_row_0):
            for j in range(0, c):
                matrix[0][j] = 0
            
       # 7.  Set entire 0th col 0 if is_row_0 true
    
        if(is_col_0):
            for i in range(0 , r):
                matrix[i][0] = 0
     
        
        
        
                