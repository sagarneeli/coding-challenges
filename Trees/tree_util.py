# A class to store a binary tree node
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
# Function to perform inOrder traversal on the tree
def inOrder(root: TreeNode):

    if root is None:
        return

    inOrder(root.left)
    print(root.data, end=' ')
    inOrder(root.right)