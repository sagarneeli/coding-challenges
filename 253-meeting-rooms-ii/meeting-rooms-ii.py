class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Time: O(NlogN)
        Space: O(N)

        """
        line_sweep = []

        for start, end in intervals:
            line_sweep.append((start, +1))
            line_sweep.append((end, -1))

        min_meetings = 0
        curr = 0
        for timestamp, tag in sorted(line_sweep):
            curr += tag
            min_meetings = max(min_meetings, curr)

        return min_meetings
        