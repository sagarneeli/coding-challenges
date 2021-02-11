"""
Reference - https://practice.geeksforgeeks.org/problems/image-multiplication/0

Problem Statement:
You are given a binary tree. Your task is pretty straightforward. 
You have to find the sum of the product of each node and its mirror image (The mirror of a node is a node which exists at the mirror position of the node in opposite subtree at the root.). 
Don’t take into account a pair more than once. 
The root node is the mirror image of itself. 

Input:
The first line consists of an integer T denoting the number of test cases. 
Each test case consists of two lines. 
The first line of each test case consists of a single integer N, denoting the number of edges in Binary tree. 
The next line contains the edges of the binary tree. 
Each edge consists of two integers and one character first of whose is parent node, 
second is child node and character "L" representing Left child and "R" representing the right child. 

Output:
For each test case, print in a new line the required sum. 
As the results can be large, print your result modulo 10^9 + 7
 

Constraints:
1 <= T <= 1000             
1 <= N <= 10^5
 

Example:
Input:
2

12
1 2 R 1 3 L 2 5 L 2 4 R 3 6 R 3 7 L 5 9 L 5 8 R 7 10 R 7 11 L 4 12 R 6 15 R

2
4 5 L 4 6 R

Output:
332
46

Explanation:
The tree for the 1st case is–

                                       1                  

                         /                               \

                 3                                           2

            /           \                             /            \

       7                    6                   5                   4

   /      \                    \               /       \                    \

11       10                15         9             8                 12

Sum = (1*1) + (3*2) + (7*4) + (6*5) + (11*12) + (15*9) = 332

 

The tree for the 2nd case is-      

          4         

    /            \

5                   6

Sum = (4*4) + (5*6) = 46

Either BFS or DFS should work
Algorithm BFS:
1. Get all the nodes at every level
2. For each level, pop the front and last element, 
   then multiply and add the value to the sum
3. 

For DFS
1. It follows the same approach as Symmetric Tree
2. Start from the root node and move to it's left and right child
3. For each pair of nodes (let us call them ‘node1’ and ‘node2’ which are mirror images of each other) 
   other than the pair of root and root (as root node is the image of itself)
4. Move on to [node1->left and node2->right] in one step and 
5. [node1->right and node2->left] in another step. 
6. Keep calling this recursion till the end of the tree.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def imageMultiplication(root):
    def calculate(node1, node2):
        if node1 == None and node2 == None:
            return 0
        if node1 == None or node2 == None:
            return 0

        return (node1.val * node2.val) + calculate(node1.left, node2.right) + calculate(node1.right, node2.left)
    return (root.val * root.val) + calculate(root.left, root.right)

root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.left.left.left = TreeNode(11)
root.left.left.right = TreeNode(10)
root.left.right.right = TreeNode(15)
root.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(4)
root.right.left.left = TreeNode(9)
root.right.left.right = TreeNode(8)
root.right.right.right = TreeNode(12)
print(imageMultiplication(root))

root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(6)
print(imageMultiplication(root))