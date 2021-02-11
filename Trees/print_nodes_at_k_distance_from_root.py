"""
Reference:
https://www.geeksforgeeks.org/print-nodes-at-k-distance-from-root/?ref=lbp

For example, in the below tree, 4, 5 & 8 are at distance 2 from root.
            1
          /   \
        2      3
      /  \    /
    4     5  8 

Complexity Analysis:
Time Complexity - O(N), worst case we end up visiting all the nodes.
Space Complexity - O(N)

Approach:
- Do a pre-order traversal, Root->Left->Right
- While traversing decrement K value, until you hit the base case of K == 0
"""

class Node: 
    # Constructor to create a new node 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None

class Solution:

    def printKDistant(self, root, k):
        def traverse(node, k):
            if not node:
                return
            if k == 0:
                print(node.val)

            traverse(node.left, k - 1)
            traverse(node.right, k - 1)
        traverse(root, k)


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(8) 
  
Solution().printKDistant(root, 2)