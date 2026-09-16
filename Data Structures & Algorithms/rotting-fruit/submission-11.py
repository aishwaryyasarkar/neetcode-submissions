class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = {
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        }
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        numFresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    numFresh += 1

        count = 0
        while q and numFresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for x, y in directions:
                    nr, nc = r+x, c+y

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        numFresh-=1
                        q.append((nr,nc))
            count += 1

        if numFresh > 0:
            return -1
            
        return count


