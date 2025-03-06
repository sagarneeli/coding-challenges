"""
Lookup in Sorted Range

Problem:

Given a sorted array of unique elements R, which are letters of the English alphabet, and an input character x.
The elements in R are sorted with the least element appearing first. Find the minimum r in R such that r > x.
If there is no r > x, find the first element of the array (wrap around).

Example:
R = ['c', 'f', 'j', 'p', 'v']

If x equals:
'a' → return 'c'
'c' → return 'f'
'k' → return 'p'
'v' → return 'c' (wrap around case)

Note: During an interview, DON'T copy/paste the description for this question.
Instead, just copy/paste the examples and read the description for the candidate.
The reason is that by googling "Return the smallest character that is strictly larger than the search character",
the answer is easy to find.
"""


def findInsPoint(sortedStr, x):
    left, right = 0, len(sortedStr) - 1
    result = sortedStr[0]  # Default to wrap-around case

    while left <= right:
        mid = (left + right) // 2
        if sortedStr[mid] < x:
            left = mid + 1  # Search in right half
        else:
            result = sortedStr[mid]  # Update result and search in left half
            right = mid - 1

    return result


print(findInsPoint(["c", "f", "j", "p", "v"], "a"))  # 'c'
print(findInsPoint(["c", "f", "j", "p", "v"], "c"))  # 'f'
print(findInsPoint(["c", "f", "j", "p", "v"], "k"))  # 'p'
print(findInsPoint(["c", "f", "j", "p", "v"], "v"))  # 'c'
