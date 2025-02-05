class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i, j = 0, 0

        while j < N:
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                # i += 1
                # j += 1
            elif nums[i] != 0 and i < j:
                i += 1
            else:
                j += 1

        