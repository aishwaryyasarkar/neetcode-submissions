class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        inf=2147483647
        # visited = set()
        q = deque()

        # push to queue upfront
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c,0))

        while q:
            r, c, dist = q.popleft() # curr


            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] and grid[nr][nc]==inf:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc, dist+1))


        