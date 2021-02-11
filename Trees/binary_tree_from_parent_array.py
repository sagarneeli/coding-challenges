"""
Reference - https://www.geeksforgeeks.org/construct-a-binary-tree-from-parent-array-representation/

Input: parent[] = {1, 5, 5, 2, 2, -1, 3}
Output: root of below tree
          5
        /  \
       1    2
      /    / \
     0    3   4
         /
        6 
Explanation: 
Index of -1 is 5.  So 5 is root.  
5 is present at indexes 1 and 2.  So 1 and 2 are
children of 5.  
1 is present at index 0, so 0 is child of 1.
2 is present at indexes 3 and 4.  So 3 and 4 are
children of 2.  
3 is present at index 6, so 6 is child of 3.


Input: parent[] = {-1, 0, 0, 1, 1, 3, 5};
Output: root of below tree
         0
       /   \
      1     2
     / \
    3   4
   /
  5 
 /
6

Expected time complexity is O(n) where n is number of elements in given array.
"""
from tree_util import TreeNode, inOrder


class Solution:

    # Function to build a binary tree from the given parent list
    def createTree(self, parent: list) -> TreeNode:

        # Check is the parent array is empty
        if len(parent) == 0:
            return None

        # Create an empty dictionary to hold a key, value pair 
        # of (index of parent array, TreeNode(index of parent array))
        dictionary = {}

        # Create `n` new tree nodes, each having a value from 0 to `n-1`,
        # and store them in a dictionary
        for index in range(len(parent)):
            dictionary[index] = TreeNode(index)

        # Initialize a root pointer to None, 
        # we will be using this to build the tree
        root = None

        # We iterate through the parent array
        # and build our Tree with appropriate relationship
        for index, element in enumerate(parent):

            # The value of the root node index would always be -1 
            # as there is no parent for root.
            # Therefore if the parent is -1, 
            # set the root to the current node having the value `i` 
            # (stored in `dict[i]`)
            if element == -1:
                root = dictionary[index]
            else:
                # Grab the parent node correspoding to the current element
                # and assign a temporary pointer
                temp_parent = dictionary[element]
                # Get the node corresponding to the current element
                # from our dictionary
                new_node = dictionary[index]
                
                # if the parent's left child is empty, map the node to it
                if not temp_parent.left:
                    temp_parent.left = new_node
                # if the parent's left child is filled, map the node to its right child
                else:
                    temp_parent.right = new_node
        
        # return root of the constructed tree
        return root


if __name__ == '__main__':
    parent = [-1, 0, 0, 1, 2, 2, 4, 4]

    root = Solution().createTree(parent)
    inOrder(root)
