import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        heap = []
        heapq.heapify(heap)

        intervals.sort()

        sorted_queries = []
        for i, val in enumerate(queries):
            sorted_queries.append((val, i))

        sorted_queries.sort()

        res = [-1 for _ in range(len(queries))]

        j = 0
        # [1,2,3,6,7,8]
        for q, i in sorted_queries:
            while j < len(intervals) and intervals[j][0] <= q:
                if q <= intervals[j][1]:
                    heapq.heappush(heap, ((intervals[j][1] - intervals[j][0] + 1), intervals[j][1]))
                j+=1

            # remove from heap any interval thats end is < q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            if heap: 
                res[i] = heap[0][0]

        return res




