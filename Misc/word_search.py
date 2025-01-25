"""
You are tasked with writing a function that detects the location of a word in a 2D grid of characters. The word can start at any position in the grid, and consecutive letters in the word are either directly below or immediately to the right of the previous letter.

Write a function that accepts a grid and a word as input, and returns the coordinates of the word in the grid as a list. If the word appears multiple times, any one occurrence can be returned.

grid1 = [
    ['b', 'b', 'b', 'a', 'l', 'l', 'o', 'o'],
    ['b', 'a', 'c', 'c', 'e', 's', 'c', 'n'],
    ['a', 'l', 't', 'e', 'w', 'c', 'e', 'w'],
    ['a', 'l', 'o', 's', 's', 'e', 'c', 'c'],
    ['w', 'o', 'o', 'w', 'a', 'c', 'a', 'w'],
    ['i', 'b', 'w', 'o', 'w', 'w', 'o', 'w']
]
word1_1 = "access"      # [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]
word1_2 = "balloon"     # [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7)]
word1_3 = "wow"         # [(4, 3), (5, 3), (5, 4)] OR 
                          [(5, 2), (5, 3), (5, 4)] OR 
                          [(5, 5), (5, 6), (5, 7)]
word1_4 = "sec"         # [(3, 4), (3, 5), (3, 6)] OR 
                        # [(3, 4), (3, 5), (4, 5)]    

grid2 = [
  ['a'],
]
word2_1 = "a"

grid3 = [
    ['c', 'a'],
    ['t', 't'],
    ['h', 'a'],
    ['a', 'c'],
    ['t', 'g']
]
word3_1 = "cat"
word3_2 = "hat"

grid4 = [
    ['c', 'c', 'x', 't', 'i', 'b'],
    ['c', 'a', 't', 'n', 'i', 'i'],
    ['a', 'x', 'n', 'x', 'p', 't'],
    ['t', 'x', 'i', 'x', 't', 't']
]
word4_1 = "catnip"      # [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)] OR
                        # [(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)]


All test cases:

search(grid1, word1_1) => [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]
search(grid1, word1_2) => [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 7)]
search(grid1, word1_3) => [(4, 3), (5, 3), (5, 4)] OR 
                          [(5, 2), (5, 3), (5, 4)] OR 
                          [(5, 5), (5, 6), (5, 7)]
search(grid1, word1_4) => [(3, 4), (3, 5), (3, 6)] OR
                          [(3, 4), (3, 5), (4, 5)]                           
search(grid1, word1_5) => [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]

search(grid2, word2_1) => [(0, 0)]

search(grid3, word3_1) => [(0, 0), (0, 1), (1, 1)]
search(grid3, word3_2) => [(2, 0), (3, 0), (4, 0)]

search(grid4, word4_1) => [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)] OR
                          [(0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4)]

Complexity analysis variables:

r = number of rows
c = number of columns
w = length of the word
"""

grid1 = [
    ["b", "b", "b", "a", "l", "l", "o", "o"],
    ["b", "a", "c", "c", "e", "s", "c", "n"],
    ["a", "l", "t", "e", "w", "c", "e", "w"],
    ["a", "l", "o", "s", "s", "e", "c", "c"],
    ["w", "o", "o", "w", "a", "c", "a", "w"],
    ["i", "b", "w", "o", "w", "w", "o", "w"],
]
word1_1 = "access"
word1_2 = "balloon"
word1_3 = "wow"
word1_4 = "sec"
word1_5 = "bbaal"

grid2 = [
    ["a"],
]
word2_1 = "a"

grid3 = [
    ["c", "a"],
    ["t", "t"],
    ["h", "a"],
    ["a", "c"],
    ["t", "g"],
]
word3_1 = "cat"
word3_2 = "hat"

grid4 = [
    ["c", "c", "x", "t", "i", "b"],
    ["c", "a", "t", "n", "i", "i"],
    ["a", "x", "n", "x", "p", "t"],
    ["t", "x", "i", "x", "t", "t"],
]
word4_1 = "catnip"


def word_search(grid, word):
    ROWS = len(grid)
    COLS = len(grid[0])

    result = []
    memo = {}

    def dfs(r, c, index):
        if index == len(word):
            return True

        if (r, c, index) in memo:
            return memo[(r, c, index)]

        if r >= ROWS or c >= COLS or grid[r][c] != word[index]:
            return False

        memo[(r, c, index)] = True

        result.append([r, c])
        if dfs(r + 1, c, index + 1) or dfs(r, c + 1, index + 1):
            return True
        result.pop()

        memo[(r, c, index)] = False
        return False

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return result

    return []


grid1 = [
    ["b", "b", "b", "a", "l", "l", "o", "o"],
    ["b", "a", "c", "c", "e", "s", "c", "n"],
    ["a", "l", "t", "e", "w", "c", "e", "w"],
    ["a", "l", "o", "s", "s", "e", "c", "c"],
    ["w", "o", "o", "w", "a", "c", "a", "w"],
    ["i", "b", "w", "o", "w", "w", "o", "w"],
]
word1_1 = "access"

print(word_search(grid1, word1_1))
print(word_search(grid4, word4_1))

print(word_search(grid2, word2_1))

print(word_search(grid3, word3_1))
print(word_search(grid3, word3_2))
