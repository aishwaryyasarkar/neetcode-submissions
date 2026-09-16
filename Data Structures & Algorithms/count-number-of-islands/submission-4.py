class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = {
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        }
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        def dfs(r, c):
            if r >= rows or c >= cols or r<0 or c<0 or grid[r][c]=="0":
                return

            grid[r][c]="0"

            for x, y in directions:
                dfs(x+r, y+c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    num_islands += 1
                    dfs(r,c)

        return num_islands