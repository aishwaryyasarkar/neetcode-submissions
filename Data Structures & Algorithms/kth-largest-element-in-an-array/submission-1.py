import heapq

class Solution:
    """
        nums=[2,3,1,5,4], k=2
        [5]
        [4]


    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        
        for i in range(k):
            out = heapq.heappop(max_heap)

        return -out
        