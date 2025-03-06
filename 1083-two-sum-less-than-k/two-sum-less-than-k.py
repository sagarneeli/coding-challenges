from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        result = -1

        while left < right:
            total = nums[left] + nums[right]
            if total < k:
                result = max(result, total)
                left += 1
            else:
                right -= 1

        return result
