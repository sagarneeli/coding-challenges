# Coding Problems

Here you can find notebooks with [solutions](#Solutions) for various challenges that focus on algorithms and data structures found in coding interviews.

Each challenge has one or more reference solutions that are:
- Fully functional
- Unit tested
- Easy-to-understand

Notebooks also detail:
- Constraints
- Test cases
- Algorithms
- Big-O time and space complexities

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


## Notebook Structure
### Source

* Eg Leetcode, Geeksforgeeks etc

### Problem Statement

* States the problem to solve.
* Input parameters
* Output result

### Constraints

* Describes any constraints or assumptions.

### Test Cases

* Describes the general and edge test cases that will be evaluated in the unit test.

### Algorithm and notes

* Describes the pattern and technique used to solve the problem.


## Categories

Each solution/problem in this repo belongs to one of these categories:

1. [Arrays](https://github.com/sagarneeli/coding-challenges/tree/master/Arrays) - Array Manipulations, Sorting, Binary Search, Divide and Conquer, Sliding Window, etc.
2. [Linked Lists](https://github.com/sagarneeli/coding-challenges/tree/master/Linked%20Lists) - Linked List Searching, Pointer Manipulations, etc.
3. [Trees](https://github.com/sagarneeli/coding-challenges/tree/master/Trees) - Binary Search Trees, Tree Traversals: Breadth-First (Level Order) Traversal, Depth-First Traversal (Inorder, Preorder, Postorder), etc.
4. [Hashing DS](https://github.com/sagarneeli/coding-challenges/tree/master/Hashing%20DS) - Hashing Data Structures: Sets/HashSets and Dictionaries/HashMaps.
5. [Dynamic Programming](https://github.com/sagarneeli/coding-challenges/tree/master/Dynamic%20Programming) - 2D and 1D Dynamic Programming, LCS, LIS, Knapsack, etc.
6. [Strings](https://github.com/sagarneeli/coding-challenges/tree/master/Strings) - String Manipulations, Reversing, Encodings/Decodings, etc.
7. [Math](https://github.com/sagarneeli/coding-challenges/tree/master/Math) - GCD, LCM, Factorization, Geometry, Math Formulas, etc.
8. [Other](https://github.com/sagarneeli/coding-challenges/tree/master/Other) - Backtracking, BFS, DFS, Stacks, Queues, Deques, Priority Queues (Heaps), Matrices, etc.

    
## Repo Structure

```
coding-challenges             # Repo
├─ Arrays                     # Category of challenges
│  ├─ rotation.ipynb          # Solution notebook
│  ├─ compress_solution.ipynb
│  ├─ ...
├─ linked_lists
│  ├─ palindrome
│  ├─ ...
├─ ...
```


## Notebook Installation

### Jupyter Notebook

Run:

```
pip install jupyter
```

For more details on notebook installation, follow the directions [here](http://ipython.org/install.html).

More information on IPython/Jupyter Notebooks can be found [here](http://ipython.org/notebook.html).


## Running Challenges

```
$ git clone https://github.com/sagarneeli/coding-challenges.git
$ cd interactive-coding-challenges
$ jupyter notebook
```

## Contact Info

Feel free to contact me to discuss any issues, questions, or comments.

My contact info can be found on my [GitHub page](https://github.com/sagarneeli).


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
