class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)

        if N == 0:
            return 0

        result = 0
        prefix_sums = {0: 1}
        curr_sum = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            
            if diff in prefix_sums:
                result += prefix_sums[diff]

            if curr_sum in prefix_sums:
                prefix_sums[curr_sum] += 1
            else:
                prefix_sums[curr_sum] = 1
        
        return result
        
        