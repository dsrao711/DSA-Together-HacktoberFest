# Python3 Program to print DFS traversal
# from a given source vertex. DFS(int s,boolean[] visited)
# traverses vertices reachable from s.
from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a DFS of graph
    def DFS(self, s, visited):
        # Mark the source node as visited
        visited[s] = True
        # Print the visited node
        print(s, end=" ")

        for i in self.graph[s]:
            # already visited
            if visited[i] == True:
                continue
            # recur to the next neighbor node
            self.DFS(i, visited)


# Driver code
# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Depth First Traversal"
      " (starting from vertex 2)")
# Mark all the vertices as not visited
visited = [False] * (max(g.graph) + 1)
# DFS call
g.DFS(2, visited)
