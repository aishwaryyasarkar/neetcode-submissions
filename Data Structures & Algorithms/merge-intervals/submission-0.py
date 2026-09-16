class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sorting by 1st element will make sure we only compare to one before.

        ___
        _____

        ____
         _____
        
          _____
        ____
        """

        intervals.sort()
        res = []
        """
        intervals = [[1,3],[1,5],[6,7]]
        res = [[1,5],[6,7]]
        """
        for i in range(len(intervals)): # 2
            if i == 0:
                res.append(intervals[i])
                continue

            # comparison of 2 ranges
            s1, e1 = res[-1] # 1, 5
            s2, e2 = intervals[i] # 6, 7

            # atleast 1 has to be within the range of the other range, F, F, F, F
            if s1 <= s2 <= e1 or  s1 <= e2 <= e1 or s2 <= s1 <= e2 or  s2 <= e1 <= e2:
                res.pop()
                res.append([min(s1,s2),max(e1,e2)])
            else:
                res.append([s2,e2])

        return res

