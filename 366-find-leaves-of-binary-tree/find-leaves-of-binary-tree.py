# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node):
            if not node:
                return -1
                
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            curr_height = max(left_height, right_height) + 1
            if curr_height == len(result):
                result.append([])
            
            result[curr_height].append(node.val)
            return curr_height
        
        dfs(root)
        return result