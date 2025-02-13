class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return -1

        heapify(nums)
        count = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            count += 1

        return count
        