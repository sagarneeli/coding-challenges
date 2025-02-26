"""
Write a function that, given a list of integers (the integral numbers in {..., -1, 0, 1, ...})
returns the sum of the contiguous subsequence with the maximum sum.

Thus, given the sequence
a = {1, 2, -4, 1, 3, -2, 3, -1}, it should return 5.
sum({1, 3, -2, 3}) = 5.

Follow-up Questions:
1. What if you were looking for the maximum product rather than the maximum sum?(Moderate experience or higher only)
2. What if the list was an infinite stream, and you needed to report the maximum sum/product so far?
3. What if you were given a directed graph (i.e., each list element may have multiple ‘next’ elements, and there may be loops)?
4. Take in a goal value and return true if you can find a contiguous sum/product with that value, and false otherwise. Sum is probably more difficult than product in this case.

Interviewer tips:
Solutions to both should be linear, ideally single-pass for both. Be prepared to provide sample inputs to help candidates out, particularly in cases like all-negative lists. Be prepared to remind candidates that we only care about the sum, not which portion of the sequence gave that sum.

Suggested Hints:
Asking the candidate how they (as a human) approach the problem is often helpful. People usually naturally discard the right prefixes, but some candidates need help seeing that that’s what they are doing.
If they get an O(n) solution that isn’t single pass or constant memory, ask them to go over what data they need and try to only store/compute that data.
Ask the candidate to draw a running cumulative sum graph of a given input list, just as an exercise. Only use this if the candidate is struggling to break the O(n²) barrier and is starting to resort to esoteric, case-wise optimizations.
Expected Time (Good candidate): 20-25 minutes

"""

from typing import List


class Solution:
    """
    Write a function that, given a list of integers (both positive and negative)
    returns the sum of the contiguous subsequence with maximum sum.

    Thus, given the sequence (1, 2, -4, 1, 3, -2, 3, -1) it should return 5
    """

    def maxContiguousSubsequenceSum(self, arr: List[int]) -> int:
        if not arr:
            return 0

        max_sum = arr[0]
        curr_sum = arr[0]

        for num in arr[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum

    def maxContiguousSubsequenceProduct(self, arr: List[int]) -> int:
        if not arr:
            return 0

        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]

        for num in arr[1:]:
            if num < 0:
                min_product, max_product = max_product, min_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            result = max(result, max_product)

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxContiguousSubsequenceSum([1, 2, -4, 1, 3, -2, 3, -1]))  # 5
    print(solution.maxContiguousSubsequenceProduct([2, 3, -2, 4]))  # 6
    print(solution.maxContiguousSubsequenceProduct([1, 2, -3, 4]))  # 4
    print(solution.maxContiguousSubsequenceProduct([-2, -1]))  # 2
