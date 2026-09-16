class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        match = ""
        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        def dfs(i,j,k):
            if k == len(word):
                return True

            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return False
            
            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#" # mark visited

            for x, y in directions:
                if dfs(i+x,j+y,k+1): # if returns True
                    board[i][j] = temp
                    return True
            
            # undo
            board[i][j] = temp
            return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        
        return False