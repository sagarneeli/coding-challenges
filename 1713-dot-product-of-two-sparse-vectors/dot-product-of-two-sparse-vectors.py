class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i, num in enumerate(nums):
            if num != 0:
                self.pairs.append([i, num])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i, j = 0, 0

        while i < len(self.pairs) and j < len(vec.pairs):
            index1, index2 = self.pairs[i][0], vec.pairs[j][0]
            num1, num2 = self.pairs[i][1], vec.pairs[j][1]
            if index1 < index2:
                i += 1
            elif index1 > index2:
                j += 1
            else:
                result += (num1 * num2)
                i += 1
                j += 1

        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)