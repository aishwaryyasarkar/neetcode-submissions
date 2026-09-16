class Solution:
    """
    dfs on land cells
    needs to find nearest treasure chest
    cannot cross -1 cell, stop / backtrack
    fill each land with the nearest distance
    do not change land cell value if chest is not found on its path
    if dfs succesfull...
    then change value, value will increase as it comes from deep to shallow
    """
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = {
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        }

        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r, c = q.popleft()

            for x, y in directions:
                nr, nc = r+x, c+y

                if nr >= rows or nc >= cols or nr < 0 or nc < 0 or grid[nr][nc] != INF:
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr,nc))

                

