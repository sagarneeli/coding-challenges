class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        Complexity Analysis
        Let n be the size of nums, and let m be the maximum number in nums.

        Time Complexity: O(nlogm)

        The time complexity of this approach is primarily determined by the operations performed on the input array nums and the computation of digit sums. The calculateDigitSum function computes the sum of digits for a given number, which takes O(logm) time. This is because the number of digits in a number is proportional to log10m. The first loop iterates over all n elements in nums and computes their digit sums, resulting in a total time of O(nlogm).

        The second loop also iterates over all n elements in nums. For each element, it performs a push operation on a priority queue (min-heap). Since the heap size is limited to 2, each push operation takes O(1) time. Thus, this loop contributes O(n) to the time complexity.

        Finally, the third loop iterates over the digitSumGroups array, which has a size proportional to the maximum digit sum, O(logm). For each heap of size 2, it performs two pop operations and a sum computation, each taking O(1) time. This loop adds O(logm) to the time complexity. Combining all these, the overall time complexity is O(nlogm).

        Space Complexity: O(logm)
        The digitSumGroups array stores priority queues (min-heaps) for each possible digit sum. Since the maximum digit sum is proportional to logm, the size of this array is O(logm). Each heap in this array can store at most 2 elements, so the total space used is O(logm).
        """
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
        