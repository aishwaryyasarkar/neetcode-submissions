class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def createVocab(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.createVocab(w)

        directions = {
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        }

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(i, j, curr, word):
            if i >= rows or j >= cols or i < 0 or j < 0 or (i,j) in visited or board[i][j] not in curr.children:
                return
            
            # include current
            visited.add((i,j))
            curr = curr.children[board[i][j]]
            word += board[i][j]

            if curr.endOfWord:
                res.add(word)
            
            for x,y in directions:
                dfs(i+x, j+y, curr, word)

            # backtrack; undo
            visited.remove((i,j))
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")

        return list(res)
    
    