# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            nonlocal longest_consecutive_path
            
            left = dfs(node.left)
            right = dfs(node.right)

            left_consecutive_path = left + 1 if node.left and node.left.val - node.val == 1 else 1
            right_consecutive_path = right + 1 if node.right and node.right.val - node.val == 1 else 1

            length = max(left_consecutive_path, right_consecutive_path)
            longest_consecutive_path = max(longest_consecutive_path, length)

            return length
        
        longest_consecutive_path = 0
        dfs(root)
        return longest_consecutive_path
        