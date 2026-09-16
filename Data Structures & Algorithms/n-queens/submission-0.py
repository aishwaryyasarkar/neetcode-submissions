class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = []
        colSet = set()
        pos_diagSet = set()   # r + c
        neg_diagSet = set()   # r - c

        for i in range(n):
            row = []
            for j in range(n):
                row.append(".")
            board.append(row)

        def dfs(i):
            # no more Qs remaining
            if i >= n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                # is this an invalid position?
                if col in colSet or (i+col) in pos_diagSet or (i-col) in neg_diagSet:
                    continue
                # no more valid position for current row, return to backtrack
                

                # add a Queen
                board[i][col] = "Q"

                # make positions invalid for rest of rows due to this placement
                # pos diagonal, negative diagonal, vertical down
                colSet.add(col)
                pos_diagSet.add(i + col)
                neg_diagSet.add(i - col)

                dfs(i+1)

                # undo
                board[i][col] = "."
                colSet.remove(col)
                pos_diagSet.remove(i + col)
                neg_diagSet.remove(i - col)

        dfs(0)
        return res







            
