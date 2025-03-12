"""
In a binary tree, find the distance (count of edges) between 2 nodes.
        4
       / \
      2   8
     / \  / \
    1   3 6  9
         / \
        5   7

e.g.
Input: t1 = 5, t2 = 3
Output: 5

Input: t1 = 6, t2 = 4
Output: 2
    
Input: t1 = 7: t2 = 9
Output: 3                           
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distance_between_nodes(self, root: TreeNode, t1: int, t2: int) -> int:
        distance = -1

        def dfs(node):
            if not node:
                return -1

            nonlocal distance

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            if left_depth != -1 and right_depth == -1:
                if node.val == t1 or node.val == t2:
                    distance = left_depth
                return 1 + left_depth

            if left_depth == -1 and right_depth != -1:
                if node.val == t1 or node.val == t2:
                    distance = right_depth
                return 1 + right_depth

            if node.val == t1 or node.val == t2:
                return 1

            if left_depth != -1 and right_depth != -1:
                distance = left_depth + right_depth
                return left_depth + right_depth

            return -1

        dfs(root)
        return distance


# Construct Tree (from given diagram)
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root.right.left.left = TreeNode(5)
root.right.left.right = TreeNode(7)

# Test Cases
print(Solution().distance_between_nodes(root, 5, 3))  # Output: 5
print(Solution().distance_between_nodes(root, 6, 4))  # Output: 2
print(Solution().distance_between_nodes(root, 7, 9))  # Output: 3
