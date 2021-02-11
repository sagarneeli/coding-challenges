from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': []
}
visited = set()

"""
Algorithm:
1. Pick any node, visit the adjacent unvisted vertex. Mark it as visited and add it to the queue.
2. If there are no remaining adjacent vertices left, then remove the first vertex from the queue.
3. Repeat Steps 1 and 2 until the queue is empty or the desired node is found.
"""


def bfs(graph, visited, source):
    queue = deque([source])
    visited.add(source)

    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


bfs(graph, visited, 'A')
