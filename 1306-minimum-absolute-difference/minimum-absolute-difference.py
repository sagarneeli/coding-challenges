class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        result = []
        
        for i in range(len(arr) - 1):
            curr_diff = abs(arr[i + 1] - arr[i])
            if curr_diff == min_diff:
                result.append([arr[i], arr[i + 1]])
            elif curr_diff < min_diff:
                result = [[arr[i], arr[i + 1]]]
                min_diff = curr_diff

        return result

        