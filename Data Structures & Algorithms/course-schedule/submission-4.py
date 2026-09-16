class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        path = set()
        visited = set()

        for a, b in prerequisites:
            adjList[b].append(a)

        def dfs(i):
            if i >= len(adjList) or i in path:
                return False

            if i in visited:
                return True

            path.add(i) # add i to current path
            neighbors = adjList[i] # check neighbors, can be multiple

            for n in neighbors:
                if not dfs(n):
                    return False

            path.remove(i)
            visited.add(i)

            return True
        
        for n in range(len(adjList)):
            if not dfs(n):
                return False

        return True


        


