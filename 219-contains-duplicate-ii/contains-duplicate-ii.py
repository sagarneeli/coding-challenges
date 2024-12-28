class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() # Cur window of size <= k
        L = 0

        for R in range(len(nums)):
            if nums[R] in window:
                return True
            
            window.add(nums[R])
            if R - L + 1 > k:
                window.remove(nums[L])
                L += 1

        return False
        