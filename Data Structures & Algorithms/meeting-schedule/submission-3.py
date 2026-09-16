"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        count = 0

        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            count+=1

            currstart = interval.start
            currend = interval.end

            if count == 1:
                prevstart, prevend = currstart, currend
                continue

            if currstart >= prevend:
                prevstart, prevend = currstart, currend
                continue
            else:
                return False

        return True
