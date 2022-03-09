
# https://practice.geeksforgeeks.org/problems/bipartite-graph/1/#
class Solution:
    
    def dfsCheck(self , node , adj , col):
        if(col[node] == -1):
            col[node] = 1
            
        for i in adj[node]:
            if(col[i] == -1):
                col[i] = 1 - col[node]
                if(self.dfsCheck(i , adj , col) == False):
                    return False
            if(col[i] == col[node]):
                return False
                
        return True
                
    
    def isBipartite(self, V, adj):
        col = [-1]*V
        # Bfs check for every vertex 
        for i in range(0 , V):
            if(col[i] == -1):
                # If bfs check condn not satisfied
                if(self.dfsCheck(i , adj , col) == False):
                    return False
        return True
            

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isBipartite(V, adj)
        if(ans):
            print("1")
        else:
            print("0")
