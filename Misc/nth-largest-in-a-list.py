"""
Write a function that takes a list of numbers and returns the nth largest number in the list.
"""

from heapq import nlargest
import random


def nth_largest_sorting(nums: list[int], n: int) -> int:
    """
    Returns the Nth largest number in the list using sorting.
    """
    return sorted(nums, reverse=True)[n - 1]


def nth_largest_heap(nums: list[int], n: int) -> int:
    """
    Returns the Nth largest number in the list using a heap.
    """
    return nlargest(n, nums)[-1]


def nth_largest_quickselect(nums: list[int], n: int) -> int:
    """
    Returns the Nth largest number in the list using quickselect.
    """
    return quickselect(nums, 0, len(nums) - 1, n)


def quickselect(nums: list[int], left: int, right: int, k: int) -> int:
    """
    Finds the kth largest element in a list using the quickselect algorithm.
    """
    if left == right:
        return nums[left]

    pivot_index = random.randint(left, right)
    pivot_index = partition(nums, left, right, pivot_index)

    if k == len(nums) - pivot_index:
        return nums[pivot_index]
    elif k < len(nums) - pivot_index:
        return quickselect(nums, pivot_index + 1, right, k)
    else:
        return quickselect(nums, left, pivot_index - 1, k)


def partition(nums: list[int], left: int, right: int, pivot_index: int) -> int:
    """
    Partitions the list around the pivot element.
    """
    pivot_value = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store_index = left

    for i in range(left, right):
        if nums[i] < pivot_value:
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1

    nums[right], nums[store_index] = nums[store_index], nums[right]
    return store_index


if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5]
    nth = 2
    print(nth_largest_quickselect(num_list, nth))
    num_list = [1, 4, 2, 3, 6, 5, 8, 7, 9]
    nth = 4
    print(nth_largest_quickselect(num_list, nth))
