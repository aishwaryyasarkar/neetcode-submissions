class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = {
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        }

        def dfs(r, c):
            if r < 0 or c < 0 or r==rows or c==cols or board[r][c]!="O":
                return

            board[r][c] = "#"
            for x, y in directions:
                nr, nc = x+r, y+c
                dfs(nr, nc)


        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols-1]== "O":
                dfs(r, cols-1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows-1][c]== "O":
                dfs(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="#":
                    board[r][c]="O"
        