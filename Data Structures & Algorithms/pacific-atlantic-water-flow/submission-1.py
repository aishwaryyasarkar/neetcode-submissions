class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificSet, atlanticSet = set(), set()
        rows, cols = len(heights), len(heights[0])

        directions = {
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        }


        def dfs(r, c, visit, prevH):
            if (r,c) in visit or r<0 or c<0 or r==rows or c==cols or heights[r][c] < prevH:
                return

            visit.add((r,c))
            for x, y in directions:
                nr, nc = x+r, y+c
                dfs(nr,nc, visit, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pacificSet, heights[r][0])
            dfs(r, cols-1, atlanticSet, heights[r][cols-1])

        for c in range(cols):
            dfs(0, c, pacificSet, heights[0][c])
            dfs(rows-1, c, atlanticSet, heights[rows-1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacificSet and (r,c) in atlanticSet:
                    res.append([r,c])

        return res
                 