class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for _ in range(n)]
        path, visited = set(), set()

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(n, parent):
            # if n in path and n != parent: # cycle
            #     return False

            if n in visited:
                return False

            visited.add(n)

            for nei in adjList[n]:
                if nei == parent:
                    continue

                if not dfs(nei, n):
                    return False

            return True


        if dfs(0, None) and len(visited) == n:
            return True

        return False
