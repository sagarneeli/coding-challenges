class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        """
        We can iterate through the array but from the second element
        First element will be prev
        if prev % 2 == 0 and curr % 2 == 0:
            return False
        if prev % 2 == 1 and curr % 2 == 1:
            return False
        """
        prev = nums[0]

        for curr in nums[1:]:
            if prev % 2 == 0 and curr % 2 == 0:
                return False
            if prev % 2 == 1 and curr % 2 == 1:
                return False
            prev = curr
        
        return True