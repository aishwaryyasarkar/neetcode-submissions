import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjHash = {}

        for t in tickets:
            src = t[0]
            dst = t[1]
            if src not in adjHash:
                adjHash[src] = []
            heapq.heappush(adjHash[src],dst)

        print(adjHash)
        path = []
        def dfs(a):
            print(adjHash)
            while a in adjHash and adjHash[a]:
                dst = heapq.heappop(adjHash[a])
                dfs(dst)
            path.append(a)

        dfs("JFK")
        return path[::-1]
