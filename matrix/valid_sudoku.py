# https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    
    def checkUniqueRow(self , row , board):
        # check for unique row 
        f = []
        for i in range(0 , 9):
            if(board[row][i] in f):
                return False
            if(board[row][i] != "."):
                f.append(board[row][i])
        return True
    
    def checkUniqueCol(self , col , board ):
        # Check for unique col
        f = []
        for i in range(0 , 9):
            if(board[i][col] in f):
                return False
            if(board[i][col] != '.'):
                f.append(board[i][col])
        return True
    
    def checkUniqueBox(self , row , col , board):
        # Unique box
        f = []
        for i in range(0 , 3):
            for j in range(0 , 3):
                temp = board[row+i][col+j]
                if(temp in f):
                    return False
                if(temp != '.'):
                    f.append(temp)
        return True
    
    def checkValid(self , row , col , board):
        # for box , we need to check the boxes in range till that particular row and col -> row - row % 3 , col - col % 3
        if(self.checkUniqueRow(row , board) and self.checkUniqueCol(col , board) and self.checkUniqueBox(row - row % 3, col - col % 3,board)):
            return True
        return False
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(0 , 9):
            for j in range(0 , 9):
                if(self.checkValid(i , j , board)):
                    continue
                else:
                    return False
        return True
                
        
                    
        
        
                