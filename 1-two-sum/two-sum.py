class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = Counter()

        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], index]
            hashmap[num] = index
        
        return [-1. -1]

        
