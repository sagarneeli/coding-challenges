"""
Source: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Problem Statement:
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q 
as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

Example 1:
        6
      /   \
    2       8
  /   \    /  \
0      4  7     9
    /    \
   3      5
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Notes:
Definition of a BST
- Left subtree of a node N contains nodes whose values are lesser than or equal to node N's value.
- Right subtree of a node N contains nodes whose values are greater than node N's value.
- Both left and right subtrees are also BSTs.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Steps:
    1. Start traversing the tree from the root node.
    2. If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
    3. If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
    4. If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. 
       and hence we return this common node as the LCA

    Complexity Analysis:
    Time Complexity - O(N), where N is the number of nodes
    Space Complexity - O(N), the call stack
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If both p and q are lesser than parent
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If both p and q are greater than parent
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # We have found the split point, i.e. the LCA node.
        return root

    """
    Time Complexity: O(N), where NN is the number of nodes in the BST. 
                      In the worst case we might be visiting all the nodes of the BST.
    Space Complexity: O(1)

    Algorithm
    - The steps taken are also similar to approach 1. 
    - The only difference is instead of recursively calling the function, we traverse down the tree iteratively. 
    - This is possible without using a stack or recursion since we don't need to backtrace to find the LCA node. 
    - In essence of it the problem is iterative, it just wants us to find the split point. 
    - The point from where p and q won't be part of the same subtree or when one is the parent of the other.
    """
    def lowestCommonAncestorIterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            parent_val = node.val    
            if p.val < parent_val and q.val < parent_val:
                node = node.left
            if p.val > parent_val and q.val > parent_val:
                node = node.right
        return root