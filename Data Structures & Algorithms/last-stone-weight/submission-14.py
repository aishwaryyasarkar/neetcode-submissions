import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones)>=2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(stones, -(y-x))
            else:
                heapq.heappush(stones, -(x-y))

        if not stones:
            return 0
        return -stones[0]

