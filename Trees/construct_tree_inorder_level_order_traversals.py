"""
Given inorder and level-order traversals of a Binary Tree.
Construct the Binary Tree. Following is an example to illustrate the problem.

Algorithm:
Inorder traversal - Left, Root, Right
Level Order - BFS

In level order the first element in the root of the tree.
By searching the root in InOrder sequence, we can find out all the elements 
on the left side and all the elements on the right side.

The elements in the left side - InOrder left sub array
The elements in the right side - InOrder right sub array

To construct left subtree of the root, we recur for the extracted elements
from the level order traversal and left subarray of inorder tranversal

Similarly we recur for the extracted elements from the level order and
right subarray of inorder traversal and construct the right subtree.

Complexity Analysis:
Time Complexity - O(N^2)
Space Complexity - O(N)
"""

class TreeNode:
    def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

def printInorder(root):
    if not root:
        return
    
    printInorder(root.left)
    print(root.val, end = ' ')
    printInorder(root.right)

def buildTree(levelorder, inorder):
    def helper(in_left_index = 0, in_right_index = len(inorder)):
        if in_left_index == in_right_index:
            return None
        
        itemFound = None
        for item in levelorder:
            if item in inorder[in_left_index:in_right_index]:
                itemFound = item
                break

        root = TreeNode(itemFound)
        index = inorder_map[itemFound]
        root.left = helper(in_left_index, index)
        root.right = helper(index + 1, in_right_index)
        return root

    inorder_map = {}
    for key, value in enumerate(inorder):
        inorder_map[value] = key
    return helper()

levelorder = [20, 8, 22, 4, 12, 10, 14]
inorder = [4, 8, 10, 12, 14, 20, 22]

root = buildTree(levelorder, inorder)

# Let us test the build tree by
# printing Inorder traversal
print("Inorder traversal of the constructed tree is")
printInorder(root)