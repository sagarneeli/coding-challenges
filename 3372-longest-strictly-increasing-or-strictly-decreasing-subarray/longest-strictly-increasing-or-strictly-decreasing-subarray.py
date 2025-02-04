class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur_len = 1
        result = 1
        state = 0

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                if state > 0:
                    cur_len += 1
                else:
                    cur_len = 2
                    state = 1
            elif nums[i-1] > nums[i]:
                if state < 0:
                    cur_len += 1
                else:
                    cur_len = 2
                    state = -1
            else:
                curr = 1
                state = 0

            result = max(result, cur_len)

        return result
        