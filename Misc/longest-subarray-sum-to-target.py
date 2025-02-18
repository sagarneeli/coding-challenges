"""
From an array of positive integers, find the length of the longest subarray the sum of which equals
to target value. If no such subarrays exist, return -1.

Input:
arr = [7, 3, 6, 2, 4, 5, 8, 1, 10, 9]
target = 20

Output:
5

Input:
arr = [6, 10, 3, 4, 2, 2, 2]
target = 15

Output
-1
"""


def longest_subarray_sum_to_target(arr: list, target: int) -> int:
    left, right = 0, 0
    curr_sum, max_length = 0, -1

    while right < len(arr):
        curr_sum += arr[right]

        if curr_sum == target:
            max_length = max(max_length, right - left + 1)
        else:
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

        right += 1
    return max_length


# 7, 3, 6, 2, 4, 5, 8, 1, 10, 9
#                         l
#                                r

# curr_sum = 24
# max_length = 5

print(longest_subarray_sum_to_target([7, 3, 6, 2, 4, 5, 8, 1, 10, 9], 20))
print(longest_subarray_sum_to_target([7, 3, 6, 2, 4, 5, 8, 1, 1, 1], 20))
print(longest_subarray_sum_to_target([6, 10, 3, 4, 2, 2, 2], 15))
