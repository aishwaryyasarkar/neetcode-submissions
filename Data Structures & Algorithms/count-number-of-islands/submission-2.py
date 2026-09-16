class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        0 1 1 1 0
        0 1 0 1 0
        1 1 0 0 0
        0 0 0 0 0

        1
        # as soon as i get a 1, i should increment #islands; for only starting 1
        """

        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        def dfs(r, c):
            if 0<=r<=rows-1 and 0<=c<=cols-1 and grid[r][c] == "1": 
                grid[r][c] = "0" # replace 1 by 0
                left, right, up, down = r-1, r+1, c-1, c+1
                
                dfs(left, c)
                dfs(right, c)
                dfs(r, up)
                dfs(r, down)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands+=1
                    dfs(r, c) # should handle all chain of 1s and replace it with 0
                print(grid)

        return num_islands


