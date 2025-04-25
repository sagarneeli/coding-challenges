class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        L = 0
        count = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                count += 1

            while count > k:
                if nums[L] == 0:
                    count -= 1
                L += 1

            max_ones = max(max_ones, R - L + 1)
        
        return max_ones



        