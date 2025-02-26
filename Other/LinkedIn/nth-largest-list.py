"""
Write a function that, given a List returns the nth largest element in the list.

Example:
Input: [3, 2, 1, 5, 6, 4], n = 2
Output: 5

Input: [1, 4, 2, 3, 6, 5, 8, 7, 9], n = 4
Output: 6

Input: [-4, 3, -2, 6, -9], n = 3
Output: 6

Input: [2, 2, 2, 2, 2, 2, 2], n = 3
Output: 2
"""

from typing import List
from heapq import heapify, nlargest, heappop, heappush


def nth_largest(nums: List[int], n: int) -> int:
    """
    Time Complexity: O(N log N)
    Space Complexity: O(1)
    """
    nums.sort()
    return nums[-n]


def nth_largest_heap(nums: List[int], n: int) -> int:
    """
    Time Complexity: O(N + N log K), where K = min(N, n)
    Space Complexity: O(N)
    """
    heapify(nums)
    return nlargest(n, nums)[-1]


def nth_largest_heap_optimized(nums: List[int], n: int) -> int:
    """
    Time Complexity: O(N log n)
    Space Complexity: O(1)
    """
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
        if len(min_heap) > n:
            heappop(min_heap)
    return min_heap[0]


print(nth_largest([3, 2, 1, 5, 6, 4], 2))
print(nth_largest_heap([3, 2, 1, 5, 6, 4], 2))
print(nth_largest_heap_optimized([3, 2, 1, 5, 6, 4], 2))

print(nth_largest([1, 4, 2, 3, 6, 5, 8, 7, 9], 4))
print(nth_largest_heap([1, 4, 2, 3, 6, 5, 8, 7, 9], 4))
print(nth_largest_heap_optimized([1, 4, 2, 3, 6, 5, 8, 7, 9], 4))

print(nth_largest([2, 2, 2, 2, 2, 2, 2], 2))
print(nth_largest_heap([2, 2, 2, 2, 2, 2, 2], 2))
print(nth_largest_heap_optimized([2, 2, 2, 2, 2, 2, 2], 2))

print(nth_largest([-4, 3, -2, 6, -9], 3))
print(nth_largest_heap([-4, 3, -2, 6, -9], 3))
print(nth_largest_heap_optimized([-4, 3, -2, 6, -9], 3))
