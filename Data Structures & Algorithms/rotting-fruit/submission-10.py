class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])


        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2: # rottens will be the src
                    q.append((r,c, 0))
        
        if not q: # if not 2 is present
            dist = 0

        while q:
            r,c, dist = q.popleft()
            print(grid, (r,c), dist)
            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    grid[nr][nc]=2
                    q.append((nr,nc, dist+1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1

        return dist