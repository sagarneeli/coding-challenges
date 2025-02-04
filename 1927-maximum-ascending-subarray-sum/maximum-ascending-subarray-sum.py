class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = nums[0]
        curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]

            result = max(result, curr_sum)

        return result

        