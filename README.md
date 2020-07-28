Coding Problems
Here you can find solutions for various coding/algorithmic problems and many useful resources for learning algorithms and data structures.
Also, this repo will be updated with new solutions and resources from time to time.

Note that this repo is meant to be used for learning and researching purposes only and it is not meant to be used for production.

Solutions
Algorithms and data structures are not language-specific (it's true that some languages are faster, and some are easier to use), but if you are good with the logic and pseudocode, any language would be good.
So I've decided to use Python because I think it's very close to pseudocode and it's easily readable (so it'll be easy for someone from another environment to implement the same solutions).
As I said previously, all solutions are written in Python (more precisely, Python 3), using the Built-in Functions (print, len, range, sorted, sum, min, max, etc...) and a few modules from the Python Standard Library like:

math (used for constants like math.pi, math.inf and functions like math.ceil, math.floor, math.gcd, math.log, math.pow, math.sqrt, etc)
collections (used for collections.deque when there is a need for Stack or Queue data structures)
heapq (used when there is a need for Priority Queue data structure).
random (used for nondeterministic algorithms, like shuffling arrays (Fisher–Yates shuffle), sampling arrays (Reservoir sampling) and Monte Carlo methods).
So, to execute these solutions there is no need from installing any external packages.
Coding style and name conventions are described in the official PEP8 page.

Note that I'm not the author of these problems, they are from sites like LeetCode (you can find more than 40 sites like this in the Training Sites section). Only the solutions and explanations are mine.

Template
For easier navigation into the solutions, each file with a solution in this repo will have the following template:

'''
Problem Name

Problem explanation.

Input: XXX
Output: XXX
Output explanation: XXX

=========================================
Solution 1 explanation.
    Time Complexity:    O(X)
    Space Complexity:   O(X)
Solution 2 explanation.
(some of the problems are solved in more than one way)
    Time Complexity:    O(X)
    Space Complexity:   O(X)
'''


##############
# Solution 1 #
##############

def name_of_solution_1(params):
    # description of code
    pass


##############
# Solution 2 #
##############

def name_of_solution_2(params):
    # description of code
    pass


###########
# Testing #
###########

# Test 1
# Correct result => 'result1'
test_val = 'example1'
print(name_of_solution_1(test_val))
print(name_of_solution_2(test_val))

# Test 2
# Correct result => 'result2'
test_val = 'example2'
print(name_of_solution_1(test_val))
print(name_of_solution_2(test_val))
Note that here I'm using the simplest way of testing, printing the results using the print method. Why? Because I think that the bigger part of the users of this repo isn't familiar with unit testing and I wanted this part to be intuitive. Btw, I strongly recommend using some unit testing framework for this kind of testing. The Python Standard Library contains a great framework for unit testing called unittest, or you can install some third-party unit testing framework like pytest.

Categories
Each solution/problem in this repo belongs to one of these categories:

Arrays - Array Manipulations, Sorting, Binary Search, Divide and Conquer, Sliding Window, etc.
Linked Lists - Linked List Searching, Pointer Manipulations, etc.
Trees - Binary Search Trees, Tree Traversals: Breadth-First (Level Order) Traversal, Depth-First Traversal (Inorder, Preorder, Postorder), etc.
Hashing DS - Hashing Data Structures: Sets/HashSets and Dictionaries/HashMaps.
Dynamic Programming - 2D and 1D Dynamic Programming, LCS, LIS, Knapsack, etc.
Strings - String Manipulations, Reversing, Encodings/Decodings, etc.
Math - GCD, LCM, Factorization, Geometry, Math Formulas, etc.
Other - Backtracking, BFS, DFS, Stacks, Queues, Deques, Priority Queues (Heaps), Matrices, etc.
