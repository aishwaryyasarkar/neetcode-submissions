# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
// BFS because we need to traverse level by level
Input: root = [1,2,3,4,null,null,null,5]
queue: [5]
out: [1, 3, 4]

Algo:
1. use a queue and use a for loop that will increase at each level, so we can determine end of each level
1
2, 3
.......

"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        self.out = []

        if not root:
            return []

        q.append(root)
        self.out.append(root.val)

        while q:
            for i in range(len(q)): # 1
                curr = q.popleft() # 4

                if curr.left:
                    q.append(curr.left) # 5

                if curr.right:
                    q.append(curr.right)
            
            if len(q)>0:
                self.out.append(q[-1].val)

        return self.out

