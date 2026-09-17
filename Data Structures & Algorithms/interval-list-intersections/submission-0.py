class Solution:
    """
    [0,2], [1,5]
    """
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        i, j = 0, 0
        res = []
        while i <= len(firstList) - 1 and j <= len(secondList) - 1:
            first = firstList[i]
            second = secondList[j]

            start = max(first[0], second[0])
            end = min(first[1], second[1])

            if start <= end:
                res.append([start, end])

            if second[1] > first[1]: # because since both lists are sorted, the smallest end one cannot have any further overlaps
                i+=1
            else:
                j+=1

        return res



        