class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                    if board[r][c]=="O":
                        q.append((r,c))
                        board[r][c]="#"

        while q:
            r,c = q.popleft()

            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc]=="O":
                    print("To be X:", nr, nc)
                    board[nr][nc]="#" # these are safe, not surrounded by X
                    q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="#":
                    board[r][c]="O"
