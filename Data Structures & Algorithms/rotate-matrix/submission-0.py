class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        matrix.reverse()
        
        for row in range(rows):
            for col in range(row + 1, cols):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col]
                )