import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num = nums
        self.k = k
        self.heap = []

        if len(self.num) > 0 and self.k>0:
            self.heapify()

    def heapify(self):
        self.heap = self.num[:self.k]
        heapq.heapify(self.heap)

        for i in range(self.k, len(self.num), 1):
            if self.num[i] > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, self.num[i])

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]



        
