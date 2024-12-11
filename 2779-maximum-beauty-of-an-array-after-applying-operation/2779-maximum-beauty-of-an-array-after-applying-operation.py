class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_beauty = 0

        for i, num in enumerate(nums):
            # Find the farthest index where the value is within the range [num, num + 2 * k]
            upper_bound = self._find_upper_bound(nums, num + 2 * k)
            # Update the maximum beauty based on the current range
            max_beauty = max(max_beauty, upper_bound - i + 1)

        return max_beauty

    def _find_upper_bound(self, arr: list[int], val: int) -> int:
        low, high, result = 0, len(arr) - 1, 0

        # Perform binary search to find the upper bound
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] <= val:
                result = mid  # Update the result and move to the right half
                low = mid + 1
            else:
                high = mid - 1  # Move to the left half

        return result
        