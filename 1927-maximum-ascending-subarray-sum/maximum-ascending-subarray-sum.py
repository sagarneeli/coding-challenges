class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                result = max(result, curr_sum)
                curr_sum = 0
            curr_sum += nums[i]

        return max(result, curr_sum)

        