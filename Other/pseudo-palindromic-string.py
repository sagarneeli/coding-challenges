"""
Find the pseudo palindromic path in a tree

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


def palindromicPath(root: TreeNode) -> bool:
    def dfs(node, s):
        if not node:
            return False

        # preorder action of the node
        if node.val not in s:
            s.add(node.val)
        else:
            s.remove(node.val)

        if not node.left and not node.right:
            if len(s) <= 1:
                return True

        left = dfs(node.left, s)
        right = dfs(node.right, s)

        if node.val not in s:
            s.add(node.val)
        else:
            s.remove(node.val)

        # postorder action of the node
        # backtracking (withdraws the action took by preorder)
        return left or right

    return dfs(root, set())


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

print(palindromicPath(root))  # True
