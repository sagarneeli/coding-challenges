class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(n):
            digit_sum = 0
            while n > 0:
                val = n % 10
                digit_sum += val
                n = n // 10
            return digit_sum
        
        digit_sum_groups = [[] for _ in range(82)]

        for num in nums:
            digit_sum = get_digit_sum(num)
            heapq.heappush(digit_sum_groups[digit_sum], num)
            if len(digit_sum_groups[digit_sum]) > 2:
                heapq.heappop(digit_sum_groups[digit_sum])

        max_pair_sum = -1
        for pairs in digit_sum_groups:
            if len(pairs) == 2:
                first = heapq.heappop(pairs)
                second = heapq.heappop(pairs)
                max_pair_sum = max(max_pair_sum, first + second)

        return max_pair_sum
        