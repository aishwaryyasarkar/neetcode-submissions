class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '0':
                    continue

                # expand
                k = 1
                while True:
                    if r + k > rows or c + k > cols:
                        break # cannot form square

                    valid = True

                    for i in range(r, r + k):
                        if matrix[i][c + k - 1] == '0':
                            valid = False
                            break
                    
                    for j in range(c, c + k):
                        if matrix[r + k - 1][j] == '0':
                            valid = False
                            break
                    
                    # for i in range(r, r + k):
                    #     for j in range(c, c + k):
                    #         if matrix[i][j] == '0':
                    #             valid = False
                    #             break
                    
                    if not valid:
                        break
                    res = max(res, k*k)
                    k+=1

        return res

                    
                        
