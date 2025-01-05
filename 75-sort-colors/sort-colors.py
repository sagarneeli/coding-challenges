class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L, m, R = 0, 0, len(nums) - 1

        while m <= R:
            if nums[m] == 0:
                nums[L], nums[m] = nums[m], nums[L]
                L += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[R] = nums[R], nums[m]
                R -= 1
            
        