class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]
        """

        # for each cell, i need to check if it is within 0 to 9 and if already visited in this row/col
        for r in range(len(board)):
            hash_set_col = set()
            # row checker
            for c in range(len(board[0])):
                # skip empty cells
                if board[r][c] == ".":
                    continue

                curr = int(board[r][c])

                # invalid number out of range
                if curr > 9 or curr < 1:
                    return False

                # add unique numbers to each set
                if curr not in hash_set_col:
                    hash_set_col.add(curr)
                else:
                    return False

        
        for c in range(len(board[0])):
            hash_set_row = set()
            # col checker
            for r in range(len(board)):
                # skip empty cells
                if board[r][c] == ".":
                    continue

                curr = int(board[r][c])

                # invalid number out of range
                if curr > 9 or curr < 1:
                    return False

                # add unique numbers to each set
                if curr not in hash_set_row:
                    hash_set_row.add(curr)
                else:
                    return False

        # for 3x3 boxes
        start_idx = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]

        for idx in start_idx:
            start_row, start_col = idx
            hash_set_sq = set()
            for r in range(start_row, start_row+3, 1):
                for c in range(start_col, start_col+3, 1):
                    # skip empty cells
                    if board[r][c] == ".":
                        continue

                    curr = int(board[r][c])

                    # invalid number out of range
                    if curr > 9 or curr < 1:
                        return False

                    # add unique numbers to each set
                    if curr not in hash_set_sq:
                        hash_set_sq.add(curr)
                    else:
                        return False

        return True
                    





                
                
