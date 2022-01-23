#https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        time = 0 
        
        for i in range(0 , len(points) - 1):
            x , y = points[i]
            x1 , y1 = points[i+1]
            time += max(abs(x1-x) , abs(y1 - y))
            
        return time
        
            