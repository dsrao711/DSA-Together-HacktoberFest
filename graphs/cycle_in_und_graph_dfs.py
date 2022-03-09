from collections import deque

class Solution:
    
    #DFS code
    def isCycleUtil(self , node , parent ,  adj , vis):
        vis[node] = 1
        for i in adj[node]:
            if(vis[i] == 0):
                if(self.isCycleUtil(i , node , adj , vis)):
                    return True
            # Condition
            elif(i != parent):
                return True
                    
        return False
    

    def isCycle(self, V, adj):
        #Code here
        vis = [0]*V
        for i in range(V):
            if(vis[i] == 0):
                if(self.isCycleUtil(i , -1 , adj , vis) == True):
                    return True
        return False

if __name__ == '__main__':

    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if(ans):
            print("1")
        else:
            print("0")

