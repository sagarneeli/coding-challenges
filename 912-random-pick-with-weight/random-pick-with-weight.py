from typing import List
import random


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0

        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        left, right = 0, len(self.prefix_sums)

        while left < right:
            mid = left + (right - left) // 2
            if self.prefix_sums[mid] == target:
                return mid
            elif self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
