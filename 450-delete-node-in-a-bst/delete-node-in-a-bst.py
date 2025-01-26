# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_min_val_node(node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr

        def dfs(node, val):
            if not node:
                return node

            if node.val > val:
                node.left = dfs(node.left, val)
            elif node.val < val:
                node.right = dfs(node.right, val)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_node = get_min_val_node(node.right)
                    node.val = min_node.val
                    node.right = dfs(node.right, min_node.val)
                
            return node

        return dfs(root, key)

        