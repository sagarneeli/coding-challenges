# presum = [-5, 5, 5, 3, 9, 15, 15, 10]


# Given an array of integer and a pivot value, move numbers less than pivot to the left of numbers greater than pivot. Place the pivot value between the group of smaller numbers and larger numbers. Return pivotIndex.
# Assume pivot is always at the first index initially
nums = [9, 2, -1, 9, 12, 4, 7, 11, 15, 9, 20]
#       9 3 5 12

# left is the first large element, right is the last small element


def partition(nums):
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[right] >= nums[0]:
            right -= 1  # pointer RIGHT is looking for an element less than pivot
        elif nums[left] <= nums[0]:
            left += 1
        else:  # nums[left] > pivot and nums[right] < pivot
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    nums[right], nums[0] = nums[0], nums[right]
    return right


partition(nums)
print(nums)

# print 10, 8, 7, 6, 5, 4, 2, 0
nums = [0, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7, 8, 8, 10, 10]
#             |             |   | |     |   |     |
target = 12
# two sum sorted. Output [[2, 10], [4, 8], [6, 6]]

# def two_sum(nums, target):
#     left, right = 0, len(nums) - 1
#     result = []
#     while left < right:
#         if nums[left] + nums[right] == target:
#             result.append((nums[left], nums[right]))
#             prev_left = nums[left]
#             prev_right = nums[right]
#             left += 1
#             right -= 1
#             curr_left = nums[left]
#             curr_right = nums[right]

#             while prev_left == curr_left:
#                 left += 1
#             while prev_right == curr_right:
#                 right -= 1

#         elif nums[left] + nums[right] < target:
#             left += 1
#         else:
#             right -= 1


def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    result = []
    while left < right:
        if (left > 0 and nums[left] == nums[left - 1]) or nums[left] + nums[
            right
        ] < target:
            left += 1

        elif (right < len(nums) - 1 and nums[right] == nums[right + 1]) or nums[
            left
        ] + nums[right] > target:
            right -= 1
        else:
            result.append((nums[left], nums[right]))
            left += 1
            right -= 1
    return result


print(two_sum(nums=nums, target=target))


# print current then skip dups
def print_unique_from_back(nums):
    print(nums[-1])
    for i in range(len(nums) - 2, -1, -1):
        if nums[i + 1] != nums[i]:
            print(nums[i])
        else:
            continue


def print_unique(nums):
    print(nums[0])
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            print(nums[i])
        else:
            continue
