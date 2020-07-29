# Coding Problems

Here you can find [solutions](#Solutions) for various coding/algorithmic problems and many useful [tips]/[patterns](#Learning-Resources) for solving common interview problems.\
Also, this repo will be updated with new solutions and resources from time to time.

*Note that this repo is meant to be used for learning and researching purposes only and it is **not** meant to be used for production.*


## Solutions

All solutions are written in [Python](https://www.python.org/) (more precisely, [Python 3](https://docs.python.org/3)), using the [Built-in Functions](https://docs.python.org/3/library/functions.html) (print, len, range, sorted, sum, min, max, etc...) and a few modules from the [Python Standard Library](https://docs.python.org/3/library/) like:
- [math](https://docs.python.org/3/library/math.html) (used for constants like math.pi, math.inf and functions like math.ceil, math.floor, math.gcd, math.log, math.pow, math.sqrt, etc)
- [collections](https://docs.python.org/3/library/collections.html) (used for [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) when there is a need for [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) or [Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) data structures)
- [heapq](https://docs.python.org/3/library/heapq.html) (used when there is a need for [Priority Queue](https://en.wikipedia.org/wiki/Priority_queue) data structure).
- [random](https://docs.python.org/3/library/random.html) (used for [nondeterministic algorithms](https://en.wikipedia.org/wiki/Nondeterministic_algorithm), like shuffling arrays ([Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)), sampling arrays ([Reservoir sampling](https://en.wikipedia.org/wiki/Reservoir_sampling)) and [Monte Carlo methods](https://en.wikipedia.org/wiki/Monte_Carlo_method)).

So, to execute these solutions there is no need from installing any external packages. \
Coding style and name conventions are described in the official [PEP8](https://www.python.org/dev/peps/pep-0008) page.

*Note that I'm **not** the author of these problems, they are from sites like [LeetCode](https://leetcode.com/) (you can find more than 40 sites like this in the [Training Sites](#Training-Sites) section). **Only** the solutions and explanations are mine.*


### Template

For easier navigation into the solutions, each file with a solution in this repo will have the following template:

```python
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
```

*Note that here I'm using the **simplest** way of testing, printing the results using the [print](https://docs.python.org/3/library/functions.html#print) method. Why? Because I think that the bigger part of the users of this repo isn't familiar with [unit testing](https://en.wikipedia.org/wiki/Unit_testing) and I wanted this part to be intuitive. Btw, I strongly recommend using some unit testing framework for this kind of testing. The Python Standard Library contains a **great** framework for unit testing called [unittest](https://docs.python.org/3/library/unittest.html), or you can install some third-party unit testing framework like [pytest](https://docs.pytest.org/en/latest/).*

### Categories

Each solution/problem in this repo belongs to one of these categories:

1. [Arrays](https://github.com/sagarneeli/coding-challenges/tree/master/Arrays) - Array Manipulations, Sorting, Binary Search, Divide and Conquer, Sliding Window, etc.
2. [Linked Lists](https://github.com/sagarneeli/coding-challenges/tree/master/Linked%20Lists) - Linked List Searching, Pointer Manipulations, etc.
3. [Trees](https://github.com/sagarneeli/coding-challenges/tree/master/Trees) - Binary Search Trees, Tree Traversals: Breadth-First (Level Order) Traversal, Depth-First Traversal (Inorder, Preorder, Postorder), etc.
4. [Hashing DS](https://github.com/sagarneeli/coding-challenges/tree/master/Hashing%20DS) - Hashing Data Structures: Sets/HashSets and Dictionaries/HashMaps.
5. [Dynamic Programming](https://github.com/sagarneeli/coding-challenges/tree/master/Dynamic%20Programming) - 2D and 1D Dynamic Programming, LCS, LIS, Knapsack, etc.
6. [Strings](https://github.com/sagarneeli/coding-challenges/tree/master/Strings) - String Manipulations, Reversing, Encodings/Decodings, etc.
7. [Math](https://github.com/sagarneeli/coding-challenges/tree/master/Math) - GCD, LCM, Factorization, Geometry, Math Formulas, etc.
8. [Other](https://github.com/sagarneeli/coding-challenges/tree/master/Other) - Backtracking, BFS, DFS, Stacks, Queues, Deques, Priority Queues (Heaps), Matrices, etc.

### Training Sites

If the problems from [LeetCode](https://leetcode.com/) are not enough and you need more problems like those, you can find much more on these platforms:

- [HackerRank](http://hackerrank.com/)
- [CodeChef](http://codechef.com/)
- [HackerEarth](http://hackerearth.com/)
- [CodeForces](http://codeforces.com/)
- [Topcoder](http://topcoder.com/)
- [Project Euler](https://projecteuler.net/)
- [SPOJ](http://www.spoj.com/)
- [A2OJ](https://a2oj.com/)
- [PEG](https://wcipeg.com/)
- [Online Judge](https://onlinejudge.org/)
- [E-Olymp](https://www.e-olymp.com/en/)
- [VJudge](https://vjudge.net/)
- [DMOJ](https://dmoj.ca/)
- [USA CO](http://www.usaco.org/)
- [Rosetta Code](http://rosettacode.org/)
- [AtCoder](https://atcoder.jp/)
- [Russian Code Cup](https://www.russiancodecup.ru/en/)
- [LintCode](http://www.lintcode.com/en/)
- [Kattis](https://www.kattis.com/developers)
- [CodeAbbey](http://codeabbey.com/)
- [CS Academy](https://csacademy.com/)
- [Advent of Code](https://adventofcode.com/)
- [Exercism](https://exercism.io/)
- [CodeFu](https://codefu.mk/)
- [Mendo](https://mendo.mk/Welcome.do)
- [Z-Training](http://www.codah.club/)
- [Codewars](http://www.codewars.com/)
- [Wolfram Challenges](https://challenges.wolfram.com/)
- [Google's Coding Competitions](https://codingcompetitions.withgoogle.com/)
- [Cyber-dojo](https://cyber-dojo.org/)
- [CodingBat](http://codingbat.com/)
- [CodeKata](http://codekata.com/)
- [BinarySearch](https://binarysearch.io/)
- [Daily Coding Problem](https://www.dailycodingproblem.com/)
- [Daily Interview Pro](http://dailyinterviewpro.com/)
- [AlgoDaily](https://algodaily.com/)
- [Codility](https://codility.com/)
- [CoderByte](https://coderbyte.com/)
- [AlgoExpert](https://www.algoexpert.io/)
- [Edabit](https://edabit.com/)
- [DevPost](https://devpost.com/)
- [Brilliant](http://brilliant.org/)
- [Codingame](https://www.codingame.com/)
- [CheckiO](http://www.checkio.org/)
- [FightCode](http://fightcodegame.com/)
- [Kaggle](http://kaggle.com/)
- [Rosalind](http://rosalind.info/problems/locations/)


### Other Resources

1. [Geeks For Geeks](https://www.geeksforgeeks.org/) - The site which **all** interested in algorithms (no matter if beginners or experts) should know! [YouTube channel](https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ) with many useful videos.
2. [The Algorithms - Python](https://github.com/TheAlgorithms/Python) - Great GitHub repo with many algorithms written in Python ([Link](https://github.com/TheAlgorithms) from the same repo written in other programming languages).
3. [CP Algorithms](http://cp-algorithms.com/) - Great page with excellent explanations for various algorithms.
4. Visualizers:
    - [USFCA Visualization Tool](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html) - Great tool for visualizing data structures and algorithms, created by the University of San Francisco.
    - [VisuAlgo](https://visualgo.net/en) - Another great tool for visualizing data structures and algorithms through animation.
    - [Algorithm Visualizer](https://algorithm-visualizer.org/) - Interactive online platform that visualizes algorithms from code. This platform is an open-source project, [here](https://github.com/algorithm-visualizer/algorithm-visualizer) you can find the source code.
