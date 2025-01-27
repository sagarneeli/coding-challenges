# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Complexity Analysis
        Time complexity : \mathcal{O}(N)O(N), where N is a number of nodes in the tree, since one visits each node exactly once.
        Space complexity : \mathcal{O}(\log(N))O(log(N)) in the best case of completely balanced tree and \mathcal{O}(N)O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.
        """
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)
            
            return left and right
        
        return dfs(p, q)
            
        