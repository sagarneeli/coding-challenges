class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                continue
            nums[i] = nums[i] * 2
            nums[i + 1] = 0
        
        i, j = 0, 0
        N = len(nums)

        while j < N:
            if nums[i] != 0 and i < j:
                i += 1
            elif nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            
        return nums
            
        