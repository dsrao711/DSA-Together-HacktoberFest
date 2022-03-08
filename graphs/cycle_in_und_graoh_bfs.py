# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1#
# https://youtu.be/A8ko93TyOns

from collections import deque

class Solution:
    
    #Function to detect cycle in an undirected graph.
    def isCycleUtil(self , adj , s , vis):
        # 1. Mark visited
        vis[s] = 1
        # 2. Parent for the first node of the component graph is -1 
        q = deque()
        q.append([s , -1])
        # 3. Traverse till q is empty
        while(q):
        # 4. Pop the front element
            node , parent = q.popleft()
        # 5. Check the adjacent nodes of the node
            for i in adj[node]:
                # 6. If unvisited , add in q
                if(vis[i] == 0):
                    q.append( [i , node])
                    vis[i] = 1
                # 7. If visited node is not parent node , cycle detected
                elif(i != parent):
                    return True
        return False
        
        
    def isCycle(self, V, adj):
        #Code here
        # Visited array 
        vis = [0]*V
        for i in range(V):
            # Find if cycle found for every component 
            if(vis[i] == 0):
                if(self.isCycleUtil(adj , i , vis) == True):
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
