# from collections import defaultdict, deque
# import heapq
# from typing import List, Optional, Type, Optional
# from heapq import heapify, heappush, heappop

# def nthlargest(nums:List[int], n: int) -> int:
#     heapify(nums)

#     while len(nums) > n:
#         heappop(nums)

#     return nums[0]

# print(nthlargest([1, 4, 2, 3, 6, 5, 8, 7, 9], 4))


# # X is some class that has an integer property `rank`.
# from typing import Callable, TypeVar
# from collections import defaultdict

# K = TypeVar("K")
# X = TypeVar("X")

# """

#      * Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
#      * retrieves it from the data source and, if possible, caches it.
#      * If the cache is full, attempt to cache the returned data,
#      * evicting the V with lowest rank among the ones that it has available.
#      * If there is a tie, the cache may choose any V with lowest rank to evict.
#      * @param key the key of the cache entry being queried
#      * @return the Rankable value of the cache entry
# """
# class Rankable:
#     """Mock Rankable class with a ranking system."""
#     def __init__(self, value, rank):
#         self.value = value
#         self.rank = rank

#     def getRank(self):
#         return self.rank  # Returns the rank of the object

#     def __repr__(self):
#         return f"Rankable(value={self.value}, rank={self.rank})"


# class DataSource:
#     """Mock DataSource to simulate slow data fetching."""
#     def __init__(self, data):
#         self.data = data  # Dictionary simulating a persistent data store

#     def get(self, key):
#         return self.data.get(key)  # Returns Rankable object or None


# class RetainBestCache(object):
#     def __init__(self, slow_process: Callable[[K], X], capacity: int):
#         self.slow_process = slow_process
#         self.capacity = capacity
#         self.cache = defaultdict()
#         self.min_heap = []

#     def get(self, key: K) -> X:
#         if key in self.cache:
#             return self.cache[key]

#         value = self.slow_process(key)
#         if len(self.cache) >= self.capacity:
#             self._evict_lowest_rank()
        
#         self.cache[key] = value
#         heappush(self.min_heap, (value.rank, key))

#         return value

#     def _evict_lowest_rank(self) -> None:
#         while self.min_heap:
#             _, key_to_remove = heappop(self.min_heap)
#             if key_to_remove in self.cache:
#                 del self.cache[key_to_remove]
#                 break

# # Slow Data Process Simulation
# def slow_process(key: str) -> Rankable:
#     data = {
#         "A": Rankable("A", 10),
#         "B": Rankable("B", 5),
#         "C": Rankable("C", 8),
#         "D": Rankable("D", 12),
#         "E": Rankable("E", 5)  # Same rank as B to test LRU behavior
#     }
#     return data.get(key, Rankable("Unkwown", 0))

# cache = RetainBestCache(slow_process=slow_process, capacity=3)

# results = {}
# results["Get A"] = cache.get("A")
# print(results)




# class Node:
#     def __init__(self, key: int = -1, val: int = -1) -> None:
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None

# class LRUCache:
#     def __init__(self, capacity: int) -> None:
#         self.capacity = capacity
#         self.head = Node()
#         self.tail = Node()
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.cache = {}

#     def _add_node(self, node: Node) -> None:
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node

#     def _remove_node(self, node: Node) -> None:
#         prev = node.prev
#         new = node.next
#         prev.next = new
#         new.prev = prev
    
#     def _move_to_head(self, node: None) -> None:
#         self._remove_node(node)
#         self._add_node(node)

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             node = self.cache[key]
#             self._move_to_head(node)
#             return node.val
#         else:
#             return -1

#     def put(self, key: int, value: int):
#         if key in self.cache:
#             node = self.cache[key]
#             node.val = value
#             self._move_to_head(node)
#         else:
#             new_node = Node(key, value)
#             self.cache[key] = new_node
#             self._add_node(new_node)
#             if len(self.cache) > self.capacity:
#                 tail = self.tail.prev
#                 self._remove_node(tail)
#                 del self.cache[tail.key]

# class Node:
#     def __init__(self, freq) -> None:
#         self.freq = freq
#         self.keys = set()
#         self.prev = None
#         self.next = None

# class AllForOne:
#     def __init__(self) -> None:
#         self.key_count = {}
#         self.freq_to_node = {}
#         self.head = Node(-1)
#         self.tail = Node(float("inf"))
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def _add_node(self, prev_node, new_node):
#         new_node.next = prev_node.next
#         new_node.prev = prev_node
#         prev_node.next.prev = new_node
#         prev_node.next = new_node

#     def _remove_node(self, node):
#         if node.keys:
#             return
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         del self.freq_to_node[node.freq]

#     def increment_key(self, key: str) -> None:
#         """
#         1. Increment the value aka freq of the key
#         2. It also increament the key_count
#         3. Update freq_to_node
#            1. Given prev freq before updating, 
#            2. get the old node and remove the key
#            3. and remove the old node as well, if its empty set of keys
#         4. Add new freq to freq_to_node map
#            1. if already a freq exists then update the keys to include in the new key
#            2. Create a mew node with the freq = key and set(key)


#         """
#         freq = self.key_count.get(key, 0)
#         new_freq = freq + 1
#         self.key_count[key] = new_freq

#         if freq in self.freq_to_node:
#             old_node = self.freq_to_node[freq]
#             old_node.keys.remove(key)
#             self._remove_node(old_node)
        
#         if new_freq in self.freq_to_node:
#             self.freq_to_node[new_freq].keys.add(key)
#         else:
#             new_node = Node(new_freq)
#             new_node.keys.add(key)
#             self.freq_to_node[new_freq] = new_node
#             self._add_node(self.freq_to_node[freq] if freq in self.freq_to_node else self.head, new_node=new_node)
            
    
#     def decrement_key(self, key: str) -> None:
#         if key not in self.key_count:
#             return
        
#         curr_freq = self.key_count[key]
#         curr_node = self.freq_to_node[curr_freq]
#         self._remove_node(curr_node)

#         new_freq = curr_freq - 1

#         if new_freq == 0:
#             del self.key_count[key]
#         else:
#             self.key_count[key] = new_freq
#             if new_freq in self.freq_to_node:
#                 self.freq_to_node[new_freq].keys.append(key)
#             else:
#                 new_node = Node(new_freq)
#                 new_node.keys.append(key)
#                 self.freq_to_node[new_freq] = new_node
#                 self._add_node(curr_node.prev, new_node=new_node)


#     def getMaxKey(self) -> int:
#         return list(self.tail.prev.keys)[0]

#     def getMinKey(self) -> int:
#         return list(self.head.next.keys)[0]


# obj = AllForOne()
# obj.increment_key("foo")
# obj.increment_key("foo")
# obj.increment_key("foo")
# obj.increment_key("foo")
# obj.increment_key("bar")
# obj.increment_key("bar")
# obj.increment_key("bar")
# # obj.increment_key("something")
# print(obj.getMaxKey())
# print(obj.getMinKey())


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None) -> None:
#         self.val = val
#         self.left = None
#         self.right = None

# def rightSideView(root: Optional[TreeNode]):
#     queue = deque([root])
#     result = []

#     while queue:
#         size = len(queue)
#         for i in range(size):
#             node = queue.popleft()

#             if i == size - 1:
#                 result.append(node.val)

#             for child in [node.left, node.right]:
#                 queue.append(child)
    
#     return result



targetSeen = False
ans = None
def inorderSuccessor(node, target):
    if not node:
        return
    if ans:
        return

    inorderSuccessor(node.left, target)
    # deal with current node
    if target == node.val:
        targetSeen = True
    if not ans and targetSeen:
        ans = node
    inorderSuccessor(node.right, target)

# Build an inorder iterator for a binary tree
# depth first search non-recursively using a stack


# from collections import Counter


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not s or not t:
#             return ""

#         t_count = Counter(t)
#         missing = len(t_count)
#         result_index, result_size = -1, len(s)
#         left, right = 0, 0

#         while right < len(s):
#             if missing > 0:
#                 ch = s[right]
#                 if ch in t_count:
#                     t_count[ch] -= 1
#                     if t_count[ch] == 0:
#                         missing -= 1
#                 right += 1
#             while missing == 0:
#                 if right - left <= result_size:
#                     result_index, result_size = left, right - left
#                 ch = s[left]
#                 if ch in t_count:
#                     t_count[ch] += 1
#                     if t_count[ch] == 1:
#                         missing += 1
#                 left += 1

#         return (
#             s[result_index : result_index + result_size] if result_size > -1 else ""
#         )


# result = Solution().minWindow("ADOBECODEBANC", "ABC")
# # print(result)



# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# # Contruction of tree
# root = Node(4)
# root.left = Node(2)
# root.left.left = Node(1)
# root.left.right = Node(3)
# root.right = Node(8)
# root.right.left = Node(6)
# root.right.left.left = Node(5)
# root.right.left.right = Node(7)
# root.right.right = Node(9)



# '''Q 1
# Find the ancestor node that is k levels above the target node in a binary tree.
# Every node's value is unique and positive.
# k and target are positive integers. 
# You are given the root node of the tree.

# e.g.
# Input1
#     target = 5
#     k = 2
# Output
#     8

# Input2
#     target = 6
#     k = 2
# Output 
#     4
    
# Input3
#     target = 7
#     k = 3
# Output 
#     4
    
# Input4
#    target = 2
#    k = 2
# Output
#    -1 (no ancestor is k levels above target)
# '''
# '''
#                  4
#              /       \
#            2          8
#          /   \      /    \          
#         1     3    6      9 
#                   /  \
#                  5    7                             
# '''
# '''Q 2
# In a binary tree, find the distance (count of edges) between 2 nodes.
# e.g.
# Input
#     t1 = 5
#     t2 = 3
# Output
#     5

# Input
#     t1 = 6
#     t2 = 4
# Output 
#     2
    
# Input
#    t1 = 7
#    t2 = 9
# Output
#    3
# '''

# '''
#                  4 lca
#              /       \
#            2(2)       8(3)
#          /   \      /    \          
#         1(-1) 3(1) 6(2)   9 
#                   /  \
#                  5(1)  7  


#     t1 = 5
#     t2 = 3                           
# '''
# def distance_between_nodes(root: Node, t1: int, t2: int) -> int:
#     distance = -1

#     def dfs(node):
#         if not node:
#             return -1
        
#         nonlocal distance

#         left_depth = dfs(node.left)
#         right_depth = dfs(node.right)
        
#         if left_depth != -1 and right_depth == -1:
#             if node.val == t1 or node.val == t2:
#                 distance = left_depth
#             return 1 + left_depth

#         if left_depth == -1 and right_depth != -1:
#             if node.val == t1 or node.val == t2:
#                 distance = right_depth
#             return 1 + right_depth

#         if node.val == t1 or node.val == t2:
#             return 1

#         if left_depth != -1 and right_depth != -1:
#             distance = left_depth + right_depth
#             return left_depth + right_depth

#         return -1

    
#     dfs(root)
#     return distance

# print(distance_between_nodes(root, 5, 3))

# def k_ancestors(root: Node, target: int, k: int) -> int:
#     kth_ancestor = -1

#     def dfs(node):
#         if not node:
#             return -1
        
#         if node.val == target:
#             return 1
            
#         nonlocal kth_ancestor

#         left_depth = dfs(node.left)
#         right_depth = dfs(node.right)
        
#         # depth = max()
#         if left_depth != -1 and right_depth == -1:
#             if k == left_depth:
#                 kth_ancestor = node.val
#             return 1 + left_depth

#         if left_depth == -1 and right_depth != -1:
#             if k == right_depth:
#                 kth_ancestor = node.val
#             return 1 + right_depth

#         return -1

    
#     dfs(root)
#     return kth_ancestor





# What templates apply to what type of tree problems preorder, postorder, extra var postorder

# Graph
# edge set
# adjacency list
# 0/1 coordinate matrix
# adjacency matrix 


# 1. Clear up input: directed graph's edge set
# 2. Come up with solution: depth first search - if graph has cycle, return false
# 3. Implementation:
    # Convert the graph input into adjacency list
    # Choose preorder vs postorder(choose postorder - cycle detection on directed graph)


# Whether the list combined of expressions is valid (not contradicting)
# Examples    
# ["a<b","b>c","c>a","d<b","e<a"]
# true

# ["a<b","b<c","c<a"]
# false

# a -> [b, c]
# d -> [e, f]

from collections import defaultdict
from typing import DefaultDict


graph = { 
1: [2],
2: [3, 4],
3: [],
4: [5, 6],
5: [6],
6: [3]
}

from collections import defaultdict
def cycle_detection(graph: dict) -> bool:
    # visited = set()

    def dfs(node, state):
        if state[node] == "visiting":
            return True
        
        if state[node] == "visited":
            return False

        state[node] = "visiting"
        
        for child in graph[node]:
            if dfs(child, state=state):
                return True

        state[node] = "visited"
        
        return False
    
    
    for node in graph.keys():
        if dfs(node, defaultdict(str)): # 'visiting' or 'visited'
            return True

    return False

print(cycle_detection(graph=graph))


# Find the value on cells of a spreadsheet
{
"D3": 10,
"C2": "D4+20",
"B4": "C2+D3"
"A1": "D3+C2+B4"
}
stack, op, num = [], '+', ""
for char in graph[node]:
    if char.isalnum():
        num += char
    else:
        if num.isdigit():
            numValue = int(num)
        else:
            numValue = dfs(num)

        if op == '+':

        elif op == '-':

        elif op == '*':

        else:
            
        op = char
        num = ""
                
graph = {
    D3: 10 #sink
    C2: [D3, 20]
    B4: [C2, D3]
    A1: [D3, C2, B4]
}
# Print out the order to figure out the var values
D3, C2, B4, A1

# If graph uncyclic, topological sort order is the reversed postorder sequence
# If the graph may be cyclic, 


from typing import List

def distinctNumbers(nums: List[int], k: int) -> List[int]:
    N = len(nums)
    window = N - k + 1
    result = []

    for end in range(N):
        if end < window:
            unique_nums = set(nums[end:end+k])
            result.append(len(unique_nums))

    return result


nums = [1,2,3,2,2,1,3]
k = 3
print(distinctNumbers(nums=nums, k=k))


nums = [1,1,1,1,2,3,4]
k = 4
print(distinctNumbers(nums=nums, k=k))


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        if i == (len(nums) - 2):
            break
        while j < k:
            if k > len(nums) - 1:
                break

            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k += 1

    return result

print(threeSum([-1,0,1,-4]))
print(threeSum([0,0,0]))
print(threeSum([1, 2, 3]))
print(threeSum([-1,0,1,2,-1,-4]))

"""
1. Sort

[-4, -1, 0, 1]
      i  
         j  
            k

- 4 - 1 + 1 = -4 < 0
- 4 + 0 + 1 = -3 < 0
-1 + 0 + 1 = 0
"""

"""
The application we're building allows users to upload a CSV containing data that we need to parse into a data structure
that we can then use to (for example) putthat data into our database.

A sample CSV file might look like:

product_id,product_name,stock_remaining\n
1,"pixel,5",55\n
2,pixelbook,31\n
3,nesthub,2\n
product_list = 
{
    1: (pixel5, 55)
    2: 
}
                        0     1
product_list["1"] => Product(pixel5, 55)
product_list["2"][1] => {pixel5: 55}
[{
    product_id: 1
    product_name: pixel5
    .../
},

]

N -> 





Write a function 
parseCSV(inputString)


 that can parse this CSV and return the parsed data in an appropriate data structure. It is up to you what data structure you choose to return the data in.
 """
from typing import List

def parseCSV(input_str: str) -> List[dict]:
    lines = input_str.split("\n")
    column_names = lines[0].split(",")
    result = []
    for line in lines[1:]:
        col_values = line.split(",")
        dictionary = {}
        for col_name, col_val in zip(column_names, col_values):
            dictionary[col_name] = col_val
        result.append(dictionary)

    return result

# string = "1,'pixel,5',55"
# print(string.split(",")) => 
# ['1', "'pixel5'", '55']

# def splitWords(line):
#     for ch in line:
input_str = "product_id,product_name,stock_remaining\n1,pixel5,55\n2,pixelbook,31\n3,nesthub,2\n"
print(parseCSV(input_str))
