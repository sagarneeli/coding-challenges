"""
Find sum of each column of tree nodes in a binary tree

Input

      2
     / \
    7    5
   / \    \
  2   6    9
     / \   /
    5  11 4 

Output

sum = [2, 12, 8, 20, 9]
       2   7  2   5  9
           5  6  11
                  4

"""

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_column(root: TreeNode) -> int:
    def dfs(node, column):
        if not node:
            return
        nonlocal leftbound, rightbound

        column_map[column].append(node.val)

        dfs(node.left, column - 1)
        dfs(node.right, column + 1)

        # update leftbound and rightbound
        leftbound = min(leftbound, column)
        rightbound = max(rightbound, column)

    column_map = defaultdict(list)
    leftbound, rightbound = 0, 0
    dfs(root, 0)

    result = []
    for column in range(leftbound, rightbound + 1):
        result.append(sum(column_map[column]))

    return result


tree_root = TreeNode(2)

tree_root.left = TreeNode(7)
tree_root.right = TreeNode(5)

tree_root.left.left = TreeNode(2)
tree_root.left.right = TreeNode(6)
tree_root.right.right = TreeNode(9)

tree_root.left.right.left = TreeNode(5)
tree_root.left.right.right = TreeNode(11)
tree_root.right.right.left = TreeNode(4)

print(sum_column(tree_root))  # [2, 12, 8, 20, 9]
