import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_hash = {}
        maxHeap = []
        q = deque()
        time = 0

        # generate frequency
        for i in range(len(tasks)):
            if tasks[i] in freq_hash:
                freq_hash[tasks[i]] -= 1
            else:
                freq_hash[tasks[i]] = -1

        # convert to max heap arr
        for val in freq_hash.values():
            maxHeap.append(val)

        # heapify
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time+=1
            if maxHeap:
                most_freq = heapq.heappop(maxHeap)
                most_freq += 1 # processed
                if most_freq < 0:
                    q.append((most_freq, time + n))


            if q and time == q[0][1]:
                pending_task = q.popleft()[0]
                heapq.heappush(maxHeap, pending_task)

        return time








