from collections import defaultdict , deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u , v):
        self.graph[u].append(v)
    def print_graph(self):
        print(self.graph)
    def bfs(self , s):
        v = len(self.graph)
        vis = [False]*v
        # Append root 
        q = deque()
        q.append(s)
        vis[s] = True
        
        while q :
            node = q.popleft()
            print(node)
            for i in self.graph[node]:
                if(vis[i] == False):
                    vis[i] = True
                    q.append(i)
                

if __name__ == '__main__' :
    graph = Graph()
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.add_edge(2,0)
    graph.add_edge(2,3)
    graph.add_edge(3,3)
    graph.print_graph()
    graph.bfs(2)
    