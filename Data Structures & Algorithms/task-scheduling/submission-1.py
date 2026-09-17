class Solution:
    """
    tasks = ["X","X","Y","Y"], n = 2
    0 1 2 3 4
    """
    import heapq
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = deque()
        freqMap = {}

        # count frequency of tasks
        for t in tasks:
            if t not in freqMap:
                freqMap[t] = 0
            freqMap[t] += 1

        # add frequencies to max heap
        for key in freqMap:
            heapq.heappush(heap, (-freqMap[key]))

        time = 0
        # process tasks
        while heap or queue:
            time += 1     

            if queue:
                # Todo: need to see if time matches cooldown
                q_freq, q_cooldown = queue[0]
                if q_cooldown == time:
                    queue.popleft()
                    heapq.heappush(heap, q_freq)

            if heap:
                freq = heapq.heappop(heap)
                freq += 1
                if freq < 0:
                    queue.append((freq, time + n + 1))
        return time
    

