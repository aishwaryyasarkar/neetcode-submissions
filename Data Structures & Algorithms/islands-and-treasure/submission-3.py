class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        inf=2147483647
        visited = set()
        q = deque()

        # push to queue upfront
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c,0))

        while q:
            r, c, dist = q.popleft() # curr
            # if r<0 or r>=rows or c<0 or c>= cols or  grid[r][c] == -1:
            #     continue 

            if (r,c) not in visited:
                print(r,c)
                if grid[r][c] == inf:
                    grid[r][c]=dist
                    visited.add((r,c))

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] and grid[nr][nc]==inf:
                        q.append((nr,nc, dist+1))
                        # # explore neighbors
                        # q.append((r, c-1, dist+1)) # left
                        # q.append((r, c+1, dist+1)) # right
                        # q.append((r-1, c, dist+1)) # up
                        # q.append((r+1, c, dist+1)) # down


        