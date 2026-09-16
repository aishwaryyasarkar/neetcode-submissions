import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjHash = {}
        for p in points:
            xi, yi = p[0], p[1]
            for q in points:
                xj, yj = q[0], q[1]
                if xi == xj and yi == yj:
                    continue
                cost = abs(xi-xj) + abs(yi-yj)
                if (xi,yi) not in adjHash:
                    adjHash[(xi,yi)]=[]
                adjHash[(xi,yi)].append((cost, [xj,yj]))

        heap = []
        heapq.heappush(heap,(0, points[0]))

        visited = set()
        cost = 0

        while heap:
            # pop
            c, src = heapq.heappop(heap)
            
            if (src[0],src[1]) in visited:
                continue

            visited.add((src[0],src[1]))
            cost+=c

            if (src[0],src[1]) in adjHash:
                for neiCost, nei in adjHash[(src[0],src[1])]:
                    if (nei[0],nei[1]) not in visited:
                        heapq.heappush(heap, (neiCost, nei))

        return cost




