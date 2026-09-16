class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        max_area=0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return 0
            grid[r][c]=0

            count=1

            count+=dfs(r,c+1)
            count+=dfs(r+1,c)
            count+=dfs(r,c-1)
            count+=dfs(r-1,c)

            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    count=dfs(r,c)
                    if count>max_area:
                        max_area=count

        return max_area