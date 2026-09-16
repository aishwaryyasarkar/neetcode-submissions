class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        cache = [[0 for i in range(cols+1)] for i in range(rows+1)]

        directions = {
            (0,1),
            (1,0),
            (1, 1),
        }
        for i in range(rows-1, -1, -1):
            for j in range(cols-1,  -1, -1):
                if matrix[i][j] == '1':
                    cache[i][j] = min(cache[i][j+1], cache[i+1][j], cache[i+1][j+1]) + 1

                res = max(res, cache[i][j])

        return res*res
  

                    
                        
