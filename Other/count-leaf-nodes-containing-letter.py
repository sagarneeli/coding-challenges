"""
Return count of leaf nodes containing a given letter in a binary tree.

Letter is a lowercase alphabet. Example i.e "n".

         (a)
        /   \
      (b)   (e)
      / \    / \
    (c) (g) (e) (n)
           /  \
         (a)  (n)

"""


class TreeNode:
    def __init__(self, val: str):
        self.val = val
        self.left = None
        self.right = None


def count_leaf_nodes(root: TreeNode, letter: str) -> int:
    def dfs(node, s):
        nonlocal count, letter

        if not node:
            return 0

        # preorder action of the node
        if node.val not in s:
            s.add(node.val)
        else:
            s.remove(node.val)

        if not node.left and not node.right:
            if node.val == letter:
                count += 1

        left = dfs(node.left, s)
        right = dfs(node.right, s)

        if node.val not in s:
            s.add(node.val)
        else:
            s.remove(node.val)

        # postorder action of the node
        # backtracking (withdraws the action took by preorder)
        return left + right

    count = 0
    dfs(root, set())
    return count


a = "a"
b = "b"
c = "c"
e = "e"
g = "g"
n = "n"

root = TreeNode(a)
root.left = TreeNode(b)
root.right = TreeNode(e)
root.left.left = TreeNode(c)
root.left.right = TreeNode(g)
root.right.left = TreeNode(e)
root.right.right = TreeNode(n)
root.right.left.left = TreeNode(a)
root.right.left.right = TreeNode(n)

print(count_leaf_nodes(root, "n"))  # True
