class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        inf=2147483647

        def bfs(r,c):
            src=(r,c) # inf
            q = deque()
            q.append((r,c, 0)) # add start node
            visited = set()
            count=0

            while q:
                r, c, dist = q.popleft() # curr

                if (r,c) not in visited:

                    if r<0 or r>=rows or c<0 or c>= cols:
                        continue 

                    visited.add((r,c)) # add curr as visited
                    if grid[r][c] == -1:
                        continue
                    
                    if grid[r][c] == 0:
                        break

                    if grid[r][c] == inf:
                        count+=1

                    # explore neighbors
                    q.append((r, c-1, dist+1)) # left
                    q.append((r, c+1, dist+1)) # right
                    q.append((r-1, c, dist+1)) # up
                    q.append((r+1, c, dist+1)) # down

            r,c=src
            grid[r][c]=dist


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==inf:
                    bfs(r,c)

        