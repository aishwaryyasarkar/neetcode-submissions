class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for i in range(n)]

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)


        visited = set()

        def dfs(i):
            if i in visited:
                return 0

            visited.add(i)

            for nei in adjList[i]:
                dfs(nei)
            return 1

        count = 0
        for i in range(n):
            count+=dfs(i)

        return count
        