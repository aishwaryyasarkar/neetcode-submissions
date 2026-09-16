class Solution:
    """
    0-1
    1-0
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        if not prerequisites:
            return True

        for i in prerequisites:
            course = i[0]
            prereq = i[1]

            if prereq not in adjList:
                adjList[prereq] = []
            adjList[prereq].append(course)

        visited = set()
        path = set()

        def dfs(n):
            # base cases
            if n in path:
                return False

            if n in visited:
                return True

            visited.add(n)
            path.add(n)

            if n in adjList:
                for nei in adjList[n]:
                    if not dfs(nei):
                        return False

            path.remove(n)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        