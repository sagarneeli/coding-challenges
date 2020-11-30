"""
Algo
- Assume we have tree T
- If tree is not null
    - If t.val is an operand we return
- Else
    A = solve(left)
    B = solve(right)
    return A operator B
    where operator is the info contained in t.

Time Comlexity - O(N)
Space Comlexity - O(N)
where N is the number of nodes in the tree.
"""
class TreeNode:
    def __init__(self, value): 
        self.left = None
        self.val = value
        self.right = None

def evaluate_expression_tree(root):
    # empty tree
    if root is None:
        return 0
    
    # Leaf Node
    if root.left is None and root.right is None:
        return int(root.val)

    # Evaluate left and right subtree
    # Post order Tree Traversal
    left = evaluate_expression_tree(root.left)
    right = evaluate_expression_tree(root.right)

    # evalute operators +, -, *, /
    if root.val == '+':
        return left + right
    if root.val == '-':
        return left - right
    if root.val == '*':
        return left * right
    return left / right


# creating a sample tree 
root = TreeNode('+') 
root.left = TreeNode('*') 
root.left.left = TreeNode('5') 
root.left.right = TreeNode('4') 
root.right = TreeNode('-') 
root.right.left = TreeNode('100') 
root.right.right = TreeNode('20') 
print(evaluate_expression_tree(root))

root = None

#creating a sample tree 
root = TreeNode('+') 
root.left = TreeNode('*') 
root.left.left = TreeNode('5') 
root.left.right = TreeNode('4') 
root.right = TreeNode('-') 
root.right.left = TreeNode('100') 
root.right.right = TreeNode('/') 
root.right.right.left = TreeNode('20') 
root.right.right.right = TreeNode('2') 
print(evaluate_expression_tree(root))


