class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for curr_start, curr_end in intervals[1:]:
            prev_start, prev_end = result[-1]

            if prev_end >= curr_start:
                result[-1][1] = max(prev_end, curr_end)
            else:
                result.append([curr_start, curr_end])

        return result
        