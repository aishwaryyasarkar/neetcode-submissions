import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Using bell-man ford
        dist = [float('inf')] * n
        temp = [float('inf')] * n
        dist[src] = 0

        for i in range(k+1):
            for u, v, w in flights:
                if dist[u] != float('inf') and dist[u] + w < temp[v]:
                    temp[v] = dist[u] + w
            dist = temp.copy()
        
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]



        # Using Dijkstra's 
        # adjHash = {}

        # for f in flights:
        #     if f[0] not in adjHash:
        #         adjHash[f[0]]=[]
        #     adjHash[f[0]].append((f[1], f[2]))

        # print(adjHash)
        # heap = [(0, src, k)]
        # heapq.heapify(heap)
        # visited = set()

        # while heap:
        #     # pop min
        #     currCost, curr, curr_k = heapq.heappop(heap)
        #     print(currCost, curr, curr_k)

        #     if (curr, curr_k) in visited:
        #         continue

        #     if curr == dst and curr_k >= -1:
        #         # print(currCost, curr, curr_k)
        #         return currCost

        #     if curr != dst and curr_k == -1:
        #         continue

        #     visited.add((curr, curr_k))

        #     if curr in adjHash:
        #         for neiAirport, neiCost in adjHash[curr]:
        #             heapq.heappush(heap, (currCost+neiCost, neiAirport, curr_k-1))

        # return -1