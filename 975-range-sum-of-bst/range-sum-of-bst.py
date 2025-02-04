# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
            TC: expression + explanation => O(N)
            SC: O(h) h: height of the tree. O(n) is the tree is skewed and when it's balanced is O(log(n))
            
        """
        def dfs(node):
            nonlocal result
            if not node:
                return
            
            if low <= node.val <= high:
                result += node.val
            if low < node.val:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        
        result = 0
        dfs(root)
        return result
        