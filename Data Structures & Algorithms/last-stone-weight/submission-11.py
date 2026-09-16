class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            val = stones[i]
            stones[i] = -val

        heapq.heapify(stones)

        # 2 heaviest
        while len(stones)>1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if -x < -y:
                heapq.heappush(stones, y-x)

        if stones:
            return stones[0] * -1
        else:
            return 0