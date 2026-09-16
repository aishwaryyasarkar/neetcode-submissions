import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adjHash = {}
        rows = len(grid)
        cols = len(grid[0])

        directions = {
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        }

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in adjHash:
                    adjHash[(r,c)]=[]
                
                for x, y in directions:
                    nr, nc = r+x, c+y
                    if 0<=nr<=rows-1 and 0<=nc<=cols-1:
                        adjHash[(r,c)].append((nr,nc))


        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)
        visited = set()


        while heap:
            # curr
            elev, r, c = heapq.heappop(heap)
            # print(elev, r, c)
            if (r,c) in visited:
                continue

            visited.add((r,c))
            if r == rows - 1 and c == cols - 1:
                return elev

            # can go to nei?
            for nei in adjHash[(r, c)]:
                nei_r, nei_c = nei[0], nei[1]
                nei_elev = grid[nei_r][nei_c]
                newTime = max(elev, nei_elev) # returns elev of nei
                heapq.heappush(heap, (newTime, nei_r, nei_c))
        
        return -1







