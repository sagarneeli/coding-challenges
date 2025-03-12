# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def dfs(node):
            nonlocal target_seen, result

            if not node or result:
                return

            dfs(node.left)

            if not result and target_seen:
                result = node
                return
            if p == node:
                target_seen = True

            dfs(node.right)
        
        target_seen = False
        result = None

        dfs(root)
        return result
            
        