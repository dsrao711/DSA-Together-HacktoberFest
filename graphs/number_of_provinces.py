#https://leetcode.com/problems/number-of-provinces/
 
from collections import defaultdict

class Solution(object):
    def dfs(self , vis , adj , node, comp):
        
        vis.add(node)
        comp.append(node)
        for i in adj[node]:
            if (i not in vis):
                self.dfs(vis , adj , i , comp)
        return comp
        
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        n = len(isConnected)
        d = defaultdict(set)
        
        # Create adj list 
        for i in range(n):
            for j in range(n):
                if(isConnected[i][j] == 1):
                    d[i+1].add(j+1)
                    d[j+1].add(i+1)
        print(d)
                        
        # DFS
        vis = set()
        op = []
        
        for i in range(1 , n+1):
            if(i not in vis):
                comp = []
                op.append(self.dfs(vis,d,i,comp))
        
        return len(op)
        
        