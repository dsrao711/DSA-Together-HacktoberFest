# Python3 Program to print Connected Components in Undirected Graph
from collections import defaultdict

# This class represents a undirected graph
# using adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Function to print a Connected Components of graph
    def connectedComponents(self):
        visited = [False] * (max(self.graph) + 1)

        component = 1
        for i in range(0, len(visited)):
            if visited[i] == False:
                print("Component No. : ", component, "-->", end="   ")
                self.DFS(i, visited)
                component += 1
                print()

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
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(4, 5)


print("Following is Depth First Traversal"
      " (starting from vertex 2)")
g.connectedComponents()
