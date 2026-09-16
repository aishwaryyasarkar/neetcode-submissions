class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        r = 0
        target_row = 0

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        while r <= n_rows:
            if target < matrix[r][n_cols-1]:
                target_row=r
                break
            elif target > matrix[r][n_cols-1]:
                r+=1
            elif target == matrix[r][n_cols-1]:
                return True

        start, end = 0, n_cols-1

        while start <= end:
            mid = start + ((end-start)+1)//2

            if target == matrix[target_row][mid]:
                return True
            elif target < matrix[target_row][mid]:
                end = mid - 1
            elif target > matrix[target_row][mid]:
                start = mid + 1
        
        return False
        
            
