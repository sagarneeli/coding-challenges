# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Use Bottom Up DFS approach
        Time Complexity
        
        The expected output is a boolean value
        But since depth is needed for the balanced check,
        consolidate boolean and depth into "int" as return type
        
        Return an int
        int == -1 => Unbalanced denotes
        int > 0 => depth of the subtree
        """
        
        def traverse(node):
            # Base Case
            # An empty tree satisfies the definition of a balanced tree
            if not node:
                return 0
            
            # General Cases / Recursive Cases
            depth_left = traverse(node.left)
            depth_right = traverse(node.right)
            
            # handle and combine left and right
            if depth_left is -1 or depth_right is -1:
                return -1
            
            # left depth and right depth differ > 1
            if abs(depth_left - depth_right) > 1:
                return -1
            
            # Current tree is balanced
            # Calculate and return depth of subtree
            return 1 + max(depth_left, depth_right)
        
        return traverse(root) != -1
        
        