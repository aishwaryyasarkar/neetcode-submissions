"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
[(0,40),(5,10),(15,20)]

0-------------------40
   5---10 15---20

heap = [20, 40]
10 < 40
20 > 10

"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        heap = []
        maxRooms = 0

        for i in intervals:
            start, end = i.start, i.end
            
            if heap:
                # peek
                last_meeting_end = heap[0]
                if last_meeting_end > start:
                    heapq.heappush(heap, end)
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, end)
            maxRooms = max(maxRooms, len(heap))

        return maxRooms




        