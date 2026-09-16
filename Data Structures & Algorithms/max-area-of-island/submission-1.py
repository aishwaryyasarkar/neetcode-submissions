class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = {
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        }

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def dfs(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c]==0:
                return 0
            
            count = 1
            grid[r][c] = 0

            for x,y in directions:
                count += dfs(r+x,c+y)

            return count
            
 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea