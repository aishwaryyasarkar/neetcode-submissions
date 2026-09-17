class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i, interval in enumerate(intervals):
            if i == 0:
                newInterval = interval
                continue

            start, end = max(newInterval[0], interval[0]), min(newInterval[1], interval[1])
            
            if end < start:
                res.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        res.append(newInterval)
        return res
        