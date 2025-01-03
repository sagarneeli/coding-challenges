class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        
        count = 0
        for i in range(n - 1):
            if prefix[i] >= prefix[-1] - prefix[i]:
                count += 1
        
        return count

        