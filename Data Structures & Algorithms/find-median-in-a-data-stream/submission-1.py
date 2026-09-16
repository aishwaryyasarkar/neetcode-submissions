import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeapLeft = []
        self.minHeapRight = []

        heapq.heapify(self.maxHeapLeft)
        heapq.heapify(self.minHeapRight)

    def addNum(self, num: int) -> None:
        if not self.maxHeapLeft or num <= -self.maxHeapLeft[0]:
            heapq.heappush(self.maxHeapLeft, -num)
        else:
            heapq.heappush(self.minHeapRight, num)

        # check if heaps are imbalanced
        if len(self.maxHeapLeft) > len(self.minHeapRight) + 1:
            val = -heapq.heappop(self.maxHeapLeft)
            heapq.heappush(self.minHeapRight, val)
        elif len(self.minHeapRight) > len(self.maxHeapLeft) + 1:
            val = heapq.heappop(self.minHeapRight)
            heapq.heappush(self.maxHeapLeft, -val)
        

    def findMedian(self) -> float:
        if len(self.maxHeapLeft) == len(self.minHeapRight):
            left = self.maxHeapLeft[0]
            right = self.minHeapRight[0]
            return (-left + right)/2 

        if len(self.maxHeapLeft) > len(self.minHeapRight):
            return -self.maxHeapLeft[0]
        else:
            return self.minHeapRight[0]
        
        