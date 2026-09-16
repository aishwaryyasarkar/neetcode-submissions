class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        for i in range(len(stones)):
            val = stones[i]
            stones[i] = -val

        heapq.heapify(stones)
        # print(stones)

        # 2 heaviest
        while True:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if -x < -y:
                heapq.heappush(stones, y-x)
            print(stones)
            if len(stones) == 1:
                out = heapq.heappop(stones)
                return -out
            
            if len(stones) == 0:
                return 0