class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # using bellman ford
        dist = [float('inf') for _ in range(n)]
        temp = [float('inf') for _ in range(n)]

        dist[src] = 0

        for _ in range(k+1):
            for u, v, w in flights:
                if dist[u] != float('inf') and dist[u] + w < temp[v]:
                    temp[v] = dist[u] + w
            dist = temp.copy()

        if dist[dst] != float('inf'):
            return dist[dst]
        else:
            return -1
                