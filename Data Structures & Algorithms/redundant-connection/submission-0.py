class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union-find
        parent = [i for i in range(len(edges)+1)]
        size = [1 for i in range(len(edges)+1)]

        def find(n):
            if n == parent[n]:
                return parent[n]
            parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            root1, root2 = find(n1), find(n2)
            if root1 == root2:
                return False

            if size[root1] > size[root2]:
                parent[root2] = root1
                size[root1] += size[root2]
            else:
                parent[root1] = root2
                size[root2] += size[root1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        


            
            



        
        