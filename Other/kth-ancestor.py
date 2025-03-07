"""
Find the ancestor node that is k levels above the target node in a binary tree.
- Every node's value is unique and positive.
- `k` and target are positive integers. 
- You are given the root node of the tree.


        4
       / \
      2   8
     / \  / \
    1   3 6  9
         / \
        5   7

        
Input1: target = 5, k = 2
Output: 8

Input2: target = 6, k = 2
Output: 4
    
Input3: target = 7, k = 3
Output: 4
    
Input4: target = 2, k = 2
Output: -1 (no ancestor is k levels above target)
"""


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def k_ancestors(self, root: TreeNode, target: int, k: int) -> int:
        kth_ancestor = -1

        def dfs(node):
            if not node:
                return -1

            if node.val == target:
                return 1  # Start depth count

            nonlocal kth_ancestor

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # Select the valid depth (whichever is non-negative)
            depth = max(left_depth, right_depth)

            if depth != -1:  # Valid depth found
                if k == depth:
                    kth_ancestor = node.val
                return depth + 1  # Increment depth

            return -1

        dfs(root)
        return kth_ancestor


# # Contruction of tree
# Renamed 'root' to 'tree_root' to avoid name conflict

tree_root = TreeNode(4)
tree_root.left = TreeNode(2)
tree_root.left.left = TreeNode(1)
tree_root.left.right = TreeNode(3)
tree_root.right = TreeNode(8)
tree_root.right.left = TreeNode(6)
tree_root.right.left.left = TreeNode(5)
tree_root.right.left.right = TreeNode(7)
tree_root.right.right = TreeNode(9)

print(Solution().k_ancestors(tree_root, 5, 2))  # Output: 8
print(Solution().k_ancestors(tree_root, 6, 2))  # Output: 4
print(Solution().k_ancestors(tree_root, 7, 3))  # Output: 4
print(Solution().k_ancestors(tree_root, 2, 2))  # Output: -1
