# https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1/#

class Solution:
    def checkCyclic(self , s , adj , vis , dfsv):
    #Function to detect cycle in a directed graph.
        vis[s] = 1
        dfsv[s] = 1
        for i in adj[s]:
            if(vis[i] == 0):
                if(self.checkCyclic(i , adj , vis , dfsv)):
                    return True
            elif(dfsv[i] == 1):
                return True
        dfsv[s] = 0
        return False
    
    def isCyclic(self, V, adj):
        # code here
        vis = [0]*V
        dfsVis = [0]*V
        for i in range(V):
            if(vis[i] == 0):
                if(self.checkCyclic(i , adj , vis , dfsVis)):
                    return True
        return False
            
    
import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
