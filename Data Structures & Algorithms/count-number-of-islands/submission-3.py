class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid) # 4
        cols=len(grid[0]) # 5
        num_islands = 0 # 1

        """
            ["0","0","0","0","0"],
            ["0","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        """

        def dfs(r, c): # 0, 1
            if 0<=r<=rows-1 and 0<=c<=cols-1 and grid[r][c]=="1":
                grid[r][c] = "0"
                dfs(r,c-1)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r+1,c)

        for r in range(rows): # 0
            for c in range(cols): # 1
                if grid[r][c]=="1":
                    num_islands+=1
                    dfs(r,c)

        return num_islands
        




