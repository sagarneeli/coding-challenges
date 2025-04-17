from collections import defaultdict, Counter, deque
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
coin_result = coin_change_greedy(coin_denominations, target_amount)
print(coin_result)


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


"""
Sliding window: Given an array where each element represents a time, count the data in the window. 
The window is defined by a time period.

a bunch of logs, each log is a [tags, timestamp, int value] structure, 
write query(String tag, int windowSize) to return the sum of a specified window size.
For example,
[ ["env:dev"], 0, 444
    ["env:dev"], 1, 300
    ["env:dev", "env:prod"], 2, 300
    ["env:prod"], 3, 400
]
query("env:dev", 2) returns 744, 600
Do you understand?
followup is to turn windowSize into a time range.

Supplementary content (2025-01-30 11:59 +08:00):
Supplement: followuop is the sum of the largest area that meets the input time interval.

tagSum(String tag, int windowSize): Returns the sum of values for a given tag within a specified window size.
"""


def tagSum(tag: str, window_size: int) -> int:
    pass


def query(tag: str, window_size: int) -> int:
    return 0


logs = [
    (["env:dev"], 0, 444),
    (["env:dev"], 1, 300),
    (["env:dev", "env:prod"], 2, 300),
    (["env:prod"], 3, 400),
]

print(query("env:dev", 2))  # returns 744, 600

"""
You're given a list of strings, where each string contains comma-separated tags
[apple, facebook, google], [banana, facebook, google], [twitter, tesla, intuit, google]

Then there's a filter list, suppose you want to find the presence of these tags based on the filter list.
For example, filter by [facebook, google] would result in [apple, tesla, intuit] (only if one has APPLE)
"""


def filter_tags(tags: List[str], filter_list: List[str]) -> List[str]:
    filter_set = set(filter_list)
    result_set = set()

    for tag_string in tags:
        tags = tag_string.replace(" ", "").split(",")
        tags_set = set(tags)

        if filter_set.issubset(tags_set):
            result_set.update(tags_set - filter_set)

    return list(result_set)


stream1 = [
    "apple, facebook, google",
    "banana, facebook",
    "facebook, google, tesla",
    "intuit, google, facebook",
]

# Test case 1
filter1 = ["apple"]
output1 = filter_tags(stream1, filter1)
print("Filter:", filter1, "-> Output:", output1)

filter2 = ["facebook", "google"]
output2 = filter_tags(stream1, filter2)
print("Filter:", filter2, "-> Output:", output2)


"""
we are given an input list containing datapoints for a metric that we receive from our customers. The input will be an object containing: tags, a timestamp and a value.

input_points = [
    { "tags": ["env:dev"], "timestamp": 0, "value": 1 },
    { "tags": ["env:dev"], "timestamp": 1, "value": 3 },
    { "tags": ["env:prod", "host:a"], "timestamp": 2, "value": 5 },
    { "tags": ["env:dev"], "timestamp": 3, "value": -1 },
    { "tags": ["env:dev", "host:a"], "timestamp": 6, "value": -3 },
    { "tags": ["env:dev"], "timestamp": 7, "value": 5 },
    { "tags": ["env:staging", "host:a"], "timestamp": 9, "value": -3 },
    { "tags": ["env:dev"], "timestamp": 10, "value": -4 },
    { "tags": ["env:dev"], "timestamp": 11, "value": 6 },
    { "tags": ["env:dev"], "timestamp": 14, "value": -1 },
    { "tags": ["env:staging"], "timestamp": 15, "value": 10 }
]

Write a function that takes an input list of datapoints, a tag t, and an integer k (window length in number of points) and return the computed sums of each consecutive window of
size k for all datapoints associated with tag t. A datapoint is associated with tag t if the tag is included along with the datapoint.

The below represents a list of datapoints (tuple containing timestamp and value) associated with tag env:dev [(0, 1), (1, 3), (3, -1), (6, -3), (7, 5), (10, -4), (11, 6), (14, -1)]

For example, if k=3 and tag=env:dev, we can consider the sliding windows of size 3 moving across these points as:

[(0, 1), (1, 3), (3, -1), (6, -3), (7, 5), (10, -4), (11, 6), (14, -1)]
((0, 1), (1, 3), (3, -1), (6, -3), (7, 5), (10, -4), (11, 6), (14, -1))
((0, 1), (1, 3), (3, -1), (6, -3), (7, 5), (10, -4), (11, 6), (14, -1))
[(0, 1), (1, 3), (3, -1), (6, -3), (7, 5), (10, -4), (11, 6), (14, -1)]
[(0, 1), (1, 3), (3, -1), (6, -3), (7, 5), (10, -4), (11, 6), (14, -1)]
[(0, 1), (1, 3), (3, -1), (6, -3), (7, 5), (10, -4), (11, 6), (14, -1)]

In the above example, the output should be [3, -1, 1, -2, 7, 1] for k=3 and tag=env:dev

"""


def compute_window_sums(datapoints, tag, k):
    # 1. Filter datapoints based on the given tag
    filtered_datapoints = [p for p in datapoints if tag in p["tags"]]
    # 2. Sort the filtered datapoints by timestamp
    filtered_datapoints.sort(key=lambda x: x["timestamp"])
    # 3. Compute the sum of each window of size k
    window = deque()
    current_sum = 0
    result = []

    for point in filtered_datapoints:
        value = point["value"]
        current_sum += value
        window.append(value)

        if len(window) > k:
            current_sum -= window.popleft()

        if len(window) == k:
            result.append(current_sum)

    return result


input_points = [
    {"tags": ["env:dev"], "timestamp": 0, "value": 1},
    {"tags": ["env:dev"], "timestamp": 1, "value": 3},
    {"tags": ["env:prod", "host:a"], "timestamp": 2, "value": 5},
    {"tags": ["env:dev"], "timestamp": 3, "value": -1},
    {"tags": ["env:dev", "host:a"], "timestamp": 6, "value": -3},
    {"tags": ["env:dev"], "timestamp": 7, "value": 5},
    {"tags": ["env:staging", "host:a"], "timestamp": 9, "value": -3},
    {"tags": ["env:dev"], "timestamp": 10, "value": -4},
    {"tags": ["env:dev"], "timestamp": 11, "value": 6},
    {"tags": ["env:dev"], "timestamp": 14, "value": -1},
    {"tags": ["env:staging"], "timestamp": 15, "value": 10},
]

# Suppose we want the sums for tag "env" over sliding windows of size 3
k = 3
output = compute_window_sums(input_points, "env:dev", k)
print(output)


from collections import Counter


def process_query_log(entries):
    queries_registered = {}  # canonical_form -> qid
    query_word_sets = {}  # qid -> set(words) for subset check
    next_qid = 1
    results = []

    for entry in entries:
        parts = entry.split(":", 1)
        entry_type = parts[0].strip()
        content = parts[1].strip()
        words = content.split()

        if entry_type == "Q":
            # Canonical form considers word counts
            word_counts = Counter(words)
            # Make it hashable for dict key
            canonical_form = frozenset(word_counts.items())

            if canonical_form not in queries_registered:
                qid = f"q{next_qid}"
                queries_registered[canonical_form] = qid
                # Store the unique words for subset checking later
                query_word_sets[qid] = set(words)
                results.append(f"Registered {qid}")
                next_qid += 1
            # else: query already registered, do nothing per interpretation

        elif entry_type == "L":
            log_word_set = set(words)
            matching_qids = []

            # Check against all registered queries
            for qid, query_set in query_word_sets.items():
                # Match if query words are a subset of log words
                if query_set.issubset(log_word_set):
                    matching_qids.append(qid)

            # Sort results for consistent output (q1 before q2 etc.)
            matching_qids.sort(key=lambda x: int(x[1:]))  # Sort numerically

            if not matching_qids:
                results.append("Log no match")
            else:
                results.append(f"Log {', '.join(matching_qids)}")

    return results


# Example Input from the screenshot
input_data = [
    "Q: hello world",
    "Q: data failure",
    "Q: world hello",  # Duplicate based on content, different order
    "L: hello world we have a data failure",
    "L: oh no hello system error",
    "Q: system error",
    "L: oh no hello system error again",
    "L: oh no hello world system error again",
]

# Run the function and print the output
# output = process_query_log(input_data)
# for line in output:
#     print(f'"{line}"')  # Formatting to match example output


from collections import Counter, defaultdict


def process_query_log_optimized(entries):
    """
    Processes query/log entries using an inverted index for potentially
    faster average-case log matching.
    """
    queries_registered = {}  # canonical_form -> qid
    query_unique_word_counts = {}  # qid -> count of unique words
    word_to_qids = defaultdict(list)  # word -> list of qids containing it
    next_qid_num = 1
    results = []

    for entry in entries:
        try:
            entry_type, content = entry.split(":", 1)
            entry_type = entry_type.strip()
            content = content.strip()
            words = content.split()
        except ValueError:
            print(f"Warning: Skipping malformed entry: {entry}")
            continue

        if not content:
            continue

        if entry_type == "Q":
            word_counts = Counter(words)
            canonical_form = frozenset(word_counts.items())

            if canonical_form not in queries_registered:
                qid = f"q{next_qid_num}"
                queries_registered[canonical_form] = qid

                query_set = set(words)
                query_unique_word_counts[qid] = len(query_set)

                # Update inverted index
                for word in query_set:
                    word_to_qids[word].append(qid)

                results.append(f"Registered {qid}")
                next_qid_num += 1
            else:
                results.append(f"Registered {queries_registered[canonical_form]}")
                # continue

        elif entry_type == "L":
            log_word_set = set(words)
            candidate_counts = Counter()
            matching_qids = []

            # Use inverted index to count potential matches
            for word in log_word_set:
                if word in word_to_qids:  # Check if word exists in any query
                    for qid in word_to_qids[word]:
                        candidate_counts[qid] += 1

            # Check candidates where count matches required unique word count
            for qid, count in candidate_counts.items():
                # Check if qid is actually registered (might be from old data if extended)
                # and if the count matches the number of unique words for that query.
                # The check `qid in query_unique_word_counts` is technically redundant
                # if the index is built correctly, but good for robustness.
                if (
                    qid in query_unique_word_counts
                    and count == query_unique_word_counts[qid]
                ):
                    matching_qids.append(qid)

            if not matching_qids:
                results.append("Log no match")
            else:
                matching_qids.sort(key=lambda x: int(x[1:]))
                results.append(f"Log {', '.join(matching_qids)}")
        else:
            print(f"Warning: Skipping unknown entry type: {entry}")
            continue

    return results


# --- Example Usage ---
input_data = [
    "Q: hello world",
    "Q: data failure",
    "Q: world hello",
    "L: hello world we have a data failure",
    "L: oh no hello system error",
    "Q: system error",
    "L: oh no hello system error again",
    "L: oh no hello world system error again",
]

output = process_query_log_optimized(input_data)

# Print the output formatted like the example
print("[")
for i, line in enumerate(output):
    print(f'  "{line}"{"," if i < len(output) - 1 else ""}')
print("]")

livetail_stream = [
    "Q: database",
    "Q: Stacktrace",
    "Q: loading failed",
    "L: Database service started",
    "Q: snapshot loading",
    "Q: fail",
    "L: Started processing events",
    "L: Loading main DB snapshot",
    "L: Loading snapshot failed no stacktrace available",
]


def word_pattern_match(word: str, pattern: str) -> bool:
    """
    1. We can use 2-pointer approach to iterate through the word and pattern
    2. Compare if the characters match in the word and pattern match
    3. If character in the pattern is a not a digit and matches the character in the word, increment both pointers
    4. If not, if check in next subsequent characters in the pattern and try to identify the word
    5. If the pattern is a digit, we can directly skip the number of characters in the word
    """
    i, j = 0, 0
    M, N = len(word), len(pattern)

    while i < M and j < N:
        if pattern[j].isdigit():
            num_str = ""
            while j < N and pattern[j].isdigit():
                num_str += pattern[j]
                j += 1
            skip = int(num_str)
            i += skip
        elif pattern[j] == "\\":
            j += 1
            if j < N and word[i] == pattern[j]:
                i += 1
                j += 1
            else:
                return False
        elif word[i] == pattern[j]:
            i += 1
            j += 1
        else:
            return False

    return i == M and j == N


# print(word_pattern_match("datadog", "d3dog"))  # True
# print(word_pattern_match("accessibility", "a11y"))  # True
# print(word_pattern_match("accessibility", "a10y"))  # False
# print(word_pattern_match("accessibility", "13"))  # True
# print(word_pattern_match("datadog", r"d\3dog"))  # False
# print(word_pattern_match("d3dog", r"d\3dog"))  # True

# Edge cases
# print(word_pattern_match("", ""))  # True - empty strings
# print(word_pattern_match("a", "1"))  # True - single character
# print(word_pattern_match("aa", "2"))  # True - multiple characters with count
# print(word_pattern_match("abc", "3"))  # True - entire word as count
# print(word_pattern_match("abc", "4"))  # False - count exceeds word length
# print(word_pattern_match("abc", "2"))  # False - count less than word length
# print(word_pattern_match("abc", "a2"))  # True - match 'a' then skip 2 characters
print(
    word_pattern_match("abc", "a1")
)  # False - count doesn't match remaining characters
print(word_pattern_match("abc", r"a\b"))  # True - escaped character match
print(word_pattern_match("ab", r"a\b"))  # True - escaped character in word
print(word_pattern_match("a1b", r"a\\b"))  # True - escaped character after digit
