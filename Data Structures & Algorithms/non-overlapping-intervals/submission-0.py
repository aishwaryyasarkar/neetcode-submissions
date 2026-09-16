class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        count = 0
        for i, interval in enumerate(intervals):
            if i == 0:
                newInterval = interval
                continue
            
            if interval[0] >= newInterval[1]:
                newInterval = interval
            else:
                if newInterval[1] > interval[1]:
                    newInterval = interval
                count+=1
        
        print(count)

        return count
