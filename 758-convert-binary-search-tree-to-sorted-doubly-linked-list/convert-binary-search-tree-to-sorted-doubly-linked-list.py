"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            if not node:
                return None, None
            
            head, tail = node, node

            head_left, tail_left = dfs(node.left)
            head_right, tail_right = dfs(node.right)

            if head_left:
                tail_left.right = node
                node.left = tail_left
                head = head_left
            
            if head_right:
                head_right.left = node
                node.right = head_right
                tail = tail_right

            return head, tail

        if not root:
            return None
        
        head, tail = dfs(root)
        tail.right = head
        head.left = tail

        return head

        