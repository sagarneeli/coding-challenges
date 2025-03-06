class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        equal = []
        greater = []

        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                lower.append(num)
  
        

        lower.extend(equal)
        lower.extend(greater)

        return lower
