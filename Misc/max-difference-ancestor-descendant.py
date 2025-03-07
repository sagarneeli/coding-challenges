"""
Find the maximum difference between an ancestor node and any of its descendant node, where (ancestor.value - descendant.value) is the maximum

        6
       /  \
      2    11
     / \   / \
   -4   1  3  -2
        / \
      -3   1

Output: 11 - (-3) = 14
maxDifference(root) → 14  (11 - (-3) = 14)
"""


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def maxDifference(self, root: TreeNode) -> int:
        def dfs(node, min_val):
            if not node:
                return float("inf"), 0  # (min_value in subtree, max_difference found)

            if not node.left and not node.right:  # Leaf node
                return node.val, 0

            left_min, left_max = dfs(node.left, min_val)
            right_min, right_max = dfs(node.right, min_val)

            # Compute the max difference
            max_diff = max(
                node.val - left_min, node.val - right_min, left_max, right_max
            )

            # Return the minimum value seen in this subtree and max difference found so far
            return min(node.val, left_min, right_min), max_diff

        _, result = dfs(root, float("inf"))
        return result


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(11)
root.left.left = TreeNode(-4)
root.left.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.right = TreeNode(-2)
root.right.left.left = TreeNode(-3)
root.right.left.right = TreeNode(1)

# Run the test
max_difference_result = Solution().maxDifference(root)
print(max_difference_result)  # Output: 14
