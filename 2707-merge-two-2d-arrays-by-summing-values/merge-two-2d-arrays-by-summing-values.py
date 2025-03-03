class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        num_map = defaultdict(int)

        for id, val in nums1:
            num_map[id] = val
        
        for id, val in nums2:
            num_map[id] += val

        result = []
        for id, val in sorted(num_map.items()):
            result.append([id, val])

        return result

        