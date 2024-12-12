class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort()
        s0, e0 = intervals[0]
        
        print(intervals)
        for  s1, e1 in intervals[1:]:
            if e0 <= s1:
                s0, e0 = s1, e1
                continue
            else:
                return False
        
        return True
                
        