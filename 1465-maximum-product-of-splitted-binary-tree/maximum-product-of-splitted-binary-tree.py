# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        # First pass: calculate total sum
        def get_total_sum(node):
            if not node:
                return 0
            left = get_total_sum(node.left)
            right = get_total_sum(node.right)
            return node.val + left + right
        
        total_sum = get_total_sum(root)
        max_product = 0
        
        # Second pass: calculate max product
        def dfs(node):
            nonlocal max_product
            if not node:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            curr_sum = left_sum + right_sum + node.val
            
            # Calculate product if we split at this subtree
            product = (total_sum - curr_sum) * curr_sum
            max_product = max(max_product, product)
            
            return curr_sum
        
        dfs(root)
        return max_product % MOD