import Graph as graph

"""
Conditions for topological-sort
1. Directed Graph
2. Acyclic
= (DAG)

Topological Sorting gives an order in which to perform the jobs. 
It's a linear ordering of vertices such that for every directed edge {u, v},
vertex 'u' comes before vertex 'v' in ordering.
"""
def topological_sort(myGraph):

