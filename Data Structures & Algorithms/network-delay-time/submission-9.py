import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}

        for i in times:
            u = i[0]
            v = i[1]
            w = i[2]
            if u not in adjList:
                adjList[u] = []
            adjList[u].append((v, w))


        heap = []
        heapq.heappush(heap, (0, k))
        visited = set()
        count = 0
        time = 0

        while heap:
            curr_time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            count+=1
            time = curr_time

            if node in adjList:
                for nei, nei_w in adjList[node]:
                    updatedTime = curr_time + nei_w
                    heapq.heappush(heap, (updatedTime, nei))
        
        if count == n:
            return time
        else:
            return -1

        