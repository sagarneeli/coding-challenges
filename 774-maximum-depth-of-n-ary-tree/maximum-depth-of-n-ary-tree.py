"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if not node:
                return 0
            if node.children == []:
                return 1
            
            result = []
            for child in node.children:
                result.append(dfs(child))
            
            return 1 + max(result)
        
        return dfs(root)
            
            


        