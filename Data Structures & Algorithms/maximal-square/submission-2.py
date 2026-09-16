class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        cache = [[float('-inf') for i in range(cols)] for i in range(rows)]

        directions = {
            (0,1),
            (1,0),
            (1, 1),
        }

        def dfs(i, j):
            nonlocal res

            if i >= rows or j >= cols:
                return 0

            if cache[i][j] != float('-inf'):
                return cache[i][j]

            minSizeSquare = float('inf')
            for x, y in directions:
                minSizeSquare = min(minSizeSquare, dfs(x+i, y+j))

            if matrix[i][j] == '1':
                cache[i][j] = minSizeSquare + 1
            else:
                cache[i][j] = 0

            res = max(res, cache[i][j])
            return cache[i][j]

        dfs(0,0)
        return res * res

                    
                        
