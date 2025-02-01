class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        Time: O(N), where N is number of items in nums
        Space: O(1)
        """
        if len(nums) == 1:
            return True
        
        prev = nums[0]

        for curr in nums[1:]:
            if prev % 2 == 0 and curr % 2 == 0:
                return False
            if prev % 2 == 1 and curr % 2 == 1:
                return False
            prev = curr
        
        return True