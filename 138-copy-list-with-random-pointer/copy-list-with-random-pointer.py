"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        visited = {None: None}

        curr = head
        while curr:
            visited[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = visited[curr]
            copy.next = visited[curr.next]
            copy.random = visited[curr.random]
            curr = curr.next

        return visited[head]

        