class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        n_rows = len(board)
        n_cols = len(board[0])
        for row in range(n_rows):
            for col in range(n_cols):
                val = board[row][col]

                if val == ".":
                    continue
                
                box = (row // 3) * 3 + (col // 3)

                if val in rows[row] or val in cols[col] or val in boxes[box]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                boxes[box].add(val)

        return True