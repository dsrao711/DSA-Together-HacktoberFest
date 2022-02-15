from collections import defaultdict

class Graph :
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self , u , v):
        self.graph[u].append(v)
        
    def dfsUtil(self , s , vis):
        stack = []
        stack.append(s)
        while(stack):
            # Pop
            node = stack.pop()
            # Mark visited
            if(vis[node] == False):
                vis[node] = True
                print(node)
            # Add elements from adj list in stack and mark visited
            for i in self.graph[node]:
                if(vis[i] == False):
                    stack.append(i)
                    vis[i] = True
    
                    
    def dfs(self):
        v = len(self.graph)
        vis = [False]*(v+1)
        
        for i in range(v):
            if(vis[i] == False):
                self.dfsUtil(i , vis)
                

if __name__ == '__main__' :
    graph = Graph()
    graph.add_edge(1, 0 )
    graph.add_edge(1, 4)
    graph.add_edge(2 , 1)
    graph.add_edge(3 , 4)
    graph.add_edge(4 , 0)
    graph.dfs()