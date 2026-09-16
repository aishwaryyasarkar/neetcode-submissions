class Solution:
    """
    Brute force:
    iterate intervals, and find i where start has just become > new start, and place interval in i - 1.
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False

        for ranges in intervals:
            if ranges[1] < newInterval[0]: # no overlap, this is on the left
                res.append(ranges)
            elif ranges[0] > newInterval[1]: # no overlap, this is on the right
                if not inserted:
                    res.append(newInterval) # insert new first
                    inserted = True
                res.append(ranges) # then the range since this is on the right
            else:
                # overlap keeps getting consumed into newInterval, not added to res yet
                newInterval[0] = min(newInterval[0], ranges[0])
                newInterval[1] = max(newInterval[1], ranges[1])
        
        # when no overlap, and ranges were all consumed in res, and newInterval still not inserted
        if not inserted:
            res.append(newInterval)

        return res

        