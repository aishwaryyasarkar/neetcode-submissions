class Solution:
    """
    1. start can be from anywhere
    2. branch out on all 4 directions
    3. in each dfs branch, 
        i. track visited // this is going to be different for each branch so it might be better to modify the element to 0 to mark visited?
        ii. only expand if not visited and if nei > curr
    4. when i, j reaches an invalid cell (out of range), return 0
    5. dfs call must return maxsize(all children) + 1 
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        directions = {
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        }
        mem = {}

        def dfs(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            
            maxChild = 0

            for x, y in directions:
                nr, nc = i+x, j+y
                if nr >= 0 and nc >= 0 and nr <= rows - 1 and nc <= cols - 1 and matrix[nr][nc] > matrix[i][j]:
                    maxChild = max(maxChild, dfs(nr, nc))

            mem[(i, j)] = maxChild + 1
            return maxChild + 1

        maxLength = 0
        for i in range(rows):
            for j in range(cols):
                maxLength = max(maxLength, dfs(i,j))

        return maxLength

        


        