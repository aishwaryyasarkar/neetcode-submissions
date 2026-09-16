import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []

        if k > len(points):
            return points

        for i in range(k):
            x = points[i][0]
            y = points[i][1]

            distance = self.getDistance(x, y)
            heapq.heappush(self.heap, (-distance, [x,y]))

        for i in range(k, len(points)):
            heap_top_distance, heap_top_point = self.heap[0]
            x = points[i][0]
            y = points[i][1]
            
            distance = self.getDistance(x, y)
            if distance < -heap_top_distance: 
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, (-distance, [x,y]))
        
        return [item[1] for item in self.heap]

    
    def getDistance(self, x_i, y_i):
        x_0, y_0 = 0, 0
        return math.sqrt((x_i - x_0)**2 + (y_i - y_0)**2)