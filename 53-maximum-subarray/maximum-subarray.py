class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]

        for num in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum
        