#https://youtu.be/6lH4nO3JfLk
# https://leetcode.com/problems/snakes-and-ladders/submissions/
from collections import deque
class Solution(object):
    
    def getCords(self , square , n):
        r = (square - 1 )//n
        c = (square - 1) % n
        if(r % 2 != 0):
            c = n - 1 - c
        return r , c
    
    def snakesAndLadders(self, board):
        """s
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        board.reverse()
        
        q = deque()
        # [square value , moves]
        q.append([1,0])
        vis = set()
        
        while(q):
            square , moves  = q.popleft()
            for i in range(1 , 7):
                nextSquare = square + i
                r , c = self.getCords(nextSquare , n)
                # Update nextSquare if snake/ladder found
                if(board[r][c] != -1):
                    nextSquare = board[r][c] 
                # If target reached
                if(nextSquare == n*n):
                    return moves + 1
                # Check if visited 
                if(nextSquare not in vis):
                    vis.add(nextSquare)
                    q.append([nextSquare , moves + 1 ])
                    
        return -1 
                
                
        
        
        
        
        