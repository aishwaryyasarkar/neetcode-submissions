"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodeMap = {}

        def dfs(curr):
            if curr in nodeMap:
                return nodeMap[curr]

            newNode = Node(curr.val)
            nodeMap[curr] = newNode

            for n in curr.neighbors:
                newNode.neighbors.append(dfs(n))

            return newNode

        return dfs(node)

        