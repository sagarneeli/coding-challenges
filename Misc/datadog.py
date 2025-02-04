from collections import defaultdict, Counter
from typing import List, Dict
import math
import re


def coin_change_greedy(coins: List[int], amount: int) -> Dict[int, int]:
    coins.sort(reverse=True)
    coin_count = defaultdict(int)

    for coin in coins:
        if amount == 0:
            break
        coin_count[coin] = amount // coin
        amount %= coin

    return coin_count if amount == 0 else {}


coin_denominations = [25, 10, 5, 1]  # Typical US coin denominations
target_amount = 63
result = coin_change_greedy(coin_denominations, target_amount)
print(result)


# Define the FileEntry base class
class FileEntry:
    """Abstract base class representing a file system entry."""

    def get_size(self):
        """Abstract method to get size; implemented in subclasses."""
        raise NotImplementedError


# Define the File subclass
class File(FileEntry):
    """Represents a file with a specific size."""

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size  # A file's size is directly returned


# Define the Directory subclass
class Directory(FileEntry):
    """Represents a directory that can contain files and other directories."""

    def __init__(self, name):
        self.name = name
        self.entries = []  # List to store FileEntry objects (Files or Directories)

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_size(self):
        """Recursively calculates the total size of all files in the directory."""
        return sum(entry.get_size() for entry in self.entries)  # Recursively sum sizes


# Function to calculate total file size within a given directory
def calculate_total_file_size(directory):
    def dfs(node):
        if isinstance(node, File):
            return node.size
        elif isinstance(node, Directory):
            totalSize = 0
            for child in node.entries:
                totalSize += dfs(child)
            return totalSize
        return 0

    return dfs(directory)


# Example Usage:
root = Directory("/home")
subdir1 = Directory("Documents")
subdir2 = Directory("Downloads")
file1 = File("file1.txt", 500)
file2 = File("file2.txt", 1000)
file3 = File("movie.mp4", 2000)
file4 = File("image.png", 750)

# Construct file system structure
subdir1.add_entry(file1)
subdir1.add_entry(file2)
subdir2.add_entry(file3)
subdir2.add_entry(file4)
root.add_entry(subdir1)
root.add_entry(subdir2)

# Calculate total file size under /home directory
total_size = calculate_total_file_size(root)
print(total_size)


def coin_change_dp(amount, coins):
    """
    DP approach: Find the minimum number of coins needed to make up the amount.
    Uses a bottom-up DP approach to find the optimal solution.
    """
    dp = [math.inf] * (amount + 1)
    dp[0] = 0  # Base case: zero amount requires zero coins

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != math.inf else -1


# Example Usage for Coin Change
coins = [25, 10, 5, 1]
amount = 63
greedy_result = coin_change_greedy(coins, amount)
dp_result = coin_change_dp(amount, coins)
print(greedy_result)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def max_path_sum_dfs(root):
    def dfs(node):
        if not node:
            return 0
        if not node.left and not node.right:
            return node.value

        left = dfs(node.left)
        right = dfs(node.right)
        return node.value + max(left, right)

    return dfs(root)


# Example Binary Tree for Path Sum
tree_root = TreeNode(10)
tree_root.left = TreeNode(5)
tree_root.right = TreeNode(20)
tree_root.left.left = TreeNode(3)
tree_root.left.right = TreeNode(7)
tree_root.right.left = TreeNode(15)
tree_root.right.right = TreeNode(25)

# Compute max path sum in a Binary Tree
tree_max_sum = max_path_sum_dfs(tree_root)
print(tree_max_sum)


class MultiTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def max_multi_tree_path_sum(root):
    def dfs(node):
        if not node:
            return 0
        if not node.children:
            return node.value
        max_child_sum = max(dfs(child) for child in node.children)
        return node.value + max_child_sum

    return dfs(root)


# Example Multi-Tree Structure
multi_root = MultiTreeNode(10)
child1 = MultiTreeNode(20)
child2 = MultiTreeNode(30)
child3 = MultiTreeNode(25)
child4 = MultiTreeNode(50)
child5 = MultiTreeNode(40)
child6 = MultiTreeNode(60)

# Construct the tree with a loop structure
multi_root.add_child(child1)
multi_root.add_child(child2)
child1.add_child(child3)
child1.add_child(child4)
child2.add_child(child5)
child2.add_child(child6)

# Compute the maximum path sum in the multi-tree
max_multi_tree_sum = max_multi_tree_path_sum(multi_root)

# Return the result
print(max_multi_tree_sum)


def count_repeated_words(paragraph):
    words = re.findall(r"\w+(?:'\w+)?", paragraph.lower())
    word_count = Counter(words)
    return {word: count for word, count in word_count.items() if count > 1}


test_paragraph = "Apple apple's banana  they're they are they're apple orange3 banana apple's Orange3 orange orange. something"
word_repetitions = count_repeated_words(test_paragraph)
print(word_repetitions)
