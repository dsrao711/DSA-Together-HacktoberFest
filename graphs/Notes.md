#### Breadth First Search or BFS for a Graph 

- Graphs are used to represent many real-life applications

- A graph is a data structure that consists of the following two components: 
    - 1. A finite set of vertices also called as nodes. 
    - 2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (u, v) is not the same as (v, u) in case of a directed graph(di-graph). The pair of the form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.


#### Depth First Search or DFS for a Graph 

- Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. 
- The only catch here is, unlike trees, graphs may contain cycles, a node may be visited twice. 
- To avoid processing a node more than once, use a boolean visited array. 

- Complexity Analysis: 
    - Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
    - Space Complexity: O(V). 
    - Since an extra visited array is needed of size V.


