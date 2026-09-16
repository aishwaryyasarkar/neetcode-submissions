class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        directions = {
            (0, 1),
            (1, 0)
        }
        mem = {}

        def dfs(i, j):
            if i == m or j == n or i < 0 or j < 0:
                return 0

            if (i == m - 1) and (j == n - 1):
                return 1

            if (i,j) in mem:
                return mem[(i,j)]

            moves = 0
            for x, y in directions:
                moves += dfs(i+x, j+y) 

            if (i,j) not in mem:
                mem[(i,j)] = 0 
            
            mem[(i,j)] = moves
            
            return moves

        return dfs(0, 0)
            

            

            
             