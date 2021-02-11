"""
Reference: - https://www.geeksforgeeks.org/clone-binary-tree-random-pointers/

Problem Statement:
Given a Binary Tree where every node has following structure.

Node {  
    key,
    Node left, right, random
} 

The random pointer points to any random node of the binary tree and can even point to NULL, 
clone the given binary tree.
"""
class Node:
    def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None
      self.random = None

def printInorder(root: 'Node'):
    if not root:
        return
    
    printInorder(root.left)
    print(root.val, end = ' ')
    printInorder(root.right)

class Solution:
    # Method 1 - Using Hashing
    def cloneRandomTree(self, tree: 'Node') -> 'Node':
        visited_dict = {}
        
        def compute(old_node):
            if old_node == None:
                return None
            
            if old_node in visited_dict:
                return visited_dict[old_node]

            new_node = Node(old_node.val)
            visited_dict[old_node] = new_node

            new_node.left = compute(old_node.left)
            new_node.right = compute(old_node.right)
            new_node.random = compute(old_node.random)
            return new_node

        return compute(tree)

# Test No 1
tree = Node(1)
tree.left = Node(2) 
tree.right = Node(3)
tree.left.left = Node(4) 
tree.left.right = Node(5)
tree.random = tree.left.right
tree.left.left.random = tree
tree.left.right.random = tree.right
cloned_tree = Solution().cloneRandomTree(tree)
print(printInorder(tree))
print(printInorder(cloned_tree))

# Test 2
tree = Node(1)
cloned_tree = Solution().cloneRandomTree(tree)
print(printInorder(tree))
print(printInorder(cloned_tree))

# Test 3
tree = Node(1)
tree.left = Node(2); 
tree.right = Node(3); 
tree.random = tree.right; 
tree.left.random = tree
cloned_tree = Solution().cloneRandomTree(tree)
print(printInorder(tree))
print(printInorder(cloned_tree))