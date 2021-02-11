from collections import defaultdict

# Class to represent a graph
class Graph:
    # Constructor
    def __init__(self, vertices):
        # dictionary containing adjacency List 
        self.graph = defaultdict(list)
        # No. of vertices
        self.vertices = vertices
    
    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)