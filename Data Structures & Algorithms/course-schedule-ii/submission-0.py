class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for i in range(numCourses)]
        
        for i, j in prerequisites:
            adjList[j].append(i)

        path, visited = set(), set()
        res = []

        def dfs(c):
            if c in path: # cycle
                return False

            if c in visited:
                return True

            path.add(c)
            neighbors = adjList[c]

            for nei in neighbors:
                if not dfs(nei):
                    return False

            res.append(c)    

            path.remove(c)
            visited.add(c)
            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res[::-1]
