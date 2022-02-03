from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        """
        if(len(grid) == 0 or grid == None):
            return 0
        
        r = len(grid)
        c = len(grid[0])
        q = deque()
        
        fresh_oranges = 0
        total_oranges = 0 
        rotten_oranges = 0
        days = 0
        flag = 0
        

        
        for i in range(0 , r):
            for j in range(0 , c):
                if(grid[i][j] == 2):
                    total_oranges += 1
                    rotten_oranges += 1
                    q.append([i , j])
                if(grid[i][j] == 1):
                    total_oranges += 1
                    
        print(total_oranges)  
        points = [-1 , -1]
        
        dx = [0 , 0 , 1, -1]
        dy = [1 , -1 , 0 , 0]
        
        while(len(q) != 0):
            
            points = q[0]
            q.popleft()
            for j in range(0 , 4):
                
                x = dx[j] + points[0]
                y = dy[j] + points[1]
                print(x , y)
                
                if(x < 0 or y < 0 or x >= r or y >= c or grid[x][y] == 2 or grid[x][y] == 0):
                    continue
                
                if(grid[x][y] == 1):
                    grid[x][y] = 2
                    rotten_oranges += 1
                    q.append([x, y])
                    flag = 1
                    
            if(flag == 1):        
                days += 1
                flag = 0
                
        print(rotten_oranges)
           
        if(rotten_oranges == total_oranges):
            return days
        else:
            return -1
        
            
                    
        
        
        