from collections import deque

class Solution:
    
    def bfsCheck(self , node , adj , col):
        # Bfs
        q = deque()
        q.append(node)
        col[node] = 1
        
        while(q):
            n = q.popleft()
            for i in adj[n]:
                # Uncolored vertex
                if(col[i] == -1):
                    # mark the adj node with opp color
                    col[i] = 1 - col[n]
                    q.append(i)
                # Adj nodes cannot be of same color
                elif(col[i] == col[n]):
                    return False
                    
        return True
    
    def isBipartite(self, V, adj):
        col = [-1]*V
        # Bfs check for every vertex 
        for i in range(0 , V):
            if(col[i] == -1):
                # If bfs check condn not satisfied
                if(self.bfsCheck(i , adj , col) == False):
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

