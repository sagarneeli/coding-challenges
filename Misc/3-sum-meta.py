"""
Given a list of positive numbers, check if there are any 3 numbers in the list,
such that a2 + b2= c2
Input
[2, 4, 6, 3, 10, 11, 5]
Output
True
32 + 42 = 52
Followup: for an array with duplicated values, print out each set of 3 eligible numbers once.
"""


def find_pythagorean_triplet(nums):
    """
    Finds Pythagorean triplets (a^2 + b^2 = c^2) in a list of numbers.

    Args:
        nums (list of int): A list of positive integers.

    Returns:
        list of list of int: A list of Pythagorean triplets found in the input list.
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 1, 1, -1):
        j, k = 0, i - 1

        while j < k:
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue

            if (nums[j] ** 2 + nums[k] ** 2) < (nums[i] ** 2):
                j += 1
            elif (nums[j] ** 2 + nums[k] ** 2) > (nums[i] ** 2):
                k -= 1
            else:
                result.append([nums[j], nums[k], nums[i]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return result


print(find_pythagorean_triplet([2, 4, 6, 3, 10, 11, 5]))
print(find_pythagorean_triplet([2, 4, 6, 3, 10, 11, 5, 10, 11, 5]))
print(find_pythagorean_triplet([3, 4, 5, 6, 8, 10]))
