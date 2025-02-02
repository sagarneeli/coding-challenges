# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Return value:
        The problem asks the total max depth, so we return the depth for the current subtree after we visit a node.
        
        State:
        To decide the depth of current node, we only need depth from its children and don't need any additional state.
        """
        def dfs(node, max_depth):
            if not node:
                return 0

            left_height = dfs(node.left, max_depth + 1)
            right_height = dfs(node.right, max_depth + 1)

            return 1 + max(left_height, right_height)
            
        return dfs(root, 0)
        