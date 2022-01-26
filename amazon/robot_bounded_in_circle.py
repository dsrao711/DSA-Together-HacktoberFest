#https://leetcode.com/problems/robot-bounded-in-circle/
# ref : https://leetcode.com/problems/robot-bounded-in-circle/
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        # Directions 
        # (Assume initially north)
        dirX = 0 
        dirY = 1 
        
        # North -> dirX = 0 , dirY = 1
        # South -> dirX = 0 , dirY = -1 
        # East  -> dirX = 1 , dirY = 0
        # West  -> dirX = -1 , dirY = 0
        
        # Position
        x , y =  0 , 0
        
        for d in instructions : 
            if(d == 'G'):
                x = x + dirX
                y = y + dirY
            if(d == 'L'): 
                # Anticlockwise
                dirX , dirY = -1*dirY , dirX
            if(d == 'R'): 
                #Clockwise
                dirX , dirY = dirY , -1*dirX
                
        # If start position == end position or if der is change in direction present
        return((x,y) == (0,0) or (dirX , dirY) != (0 , 1 ))
        
        