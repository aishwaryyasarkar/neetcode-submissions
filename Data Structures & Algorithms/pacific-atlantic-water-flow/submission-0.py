class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific_q = deque()
        atlantic_q = deque()

        p_visited = set()
        a_visited = set()

        for r in range(rows):
            pacific_q.append((r,0))
            atlantic_q.append((r,cols-1))

        for c in range(cols):
            pacific_q.append((0,c))
            atlantic_q.append((rows-1,c))

        while pacific_q:
            r,c = pacific_q.popleft()
            p_visited.add((r, c))

            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc]>=heights[r][c]:
                    if (nr,nc) not in p_visited:
                        pacific_q.append((nr, nc))

        while atlantic_q:
            r,c = atlantic_q.popleft()
            a_visited.add((r, c))

            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and heights[nr][nc]>=heights[r][c]:
                    if (nr,nc) not in a_visited:
                        atlantic_q.append((nr, nc))

        out = list(p_visited.intersection(a_visited))
        return out