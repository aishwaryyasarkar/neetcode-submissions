import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if len(times) == 0:
            return -1

        adjHash = {}

        for t in times:
            n1 = t[0]
            n2 = t[1]
            t1 = t[2]
            if n1 not in adjHash:
                adjHash[n1] = []
            adjHash[n1].append((n2,t1))

        if k not in adjHash:
            return -1

        heap = []

        heapq.heapify(heap)
        heapq.heappush(heap, (0, k))

        visited = set()
        t = 0

        while heap:
            minCost, src = heapq.heappop(heap)
            
            if src in visited:
                continue

            t=minCost
            
            visited.add(src)

            if src in adjHash:
                for nei, neiT in adjHash[src]:
                    if nei not in visited:
                        heapq.heappush(heap, (neiT+minCost, nei))

        if len(visited) == n:
            return t
        return -1


        

