# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
root = [1,2,3,4,5,6,7]
queue = [4, 5, 6, 7] 
out =[[1], [2, 3]]
curr_level = [4, 5, 6, 7]
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        out = []

        q.append(root)
        out.append([root.val])

        while q:
            curr_level = []
            for i in range(len(q)): # q.len = 2
                curr = q.popleft() # 3

                if curr.left:
                    q.append(curr.left) # 6
                    curr_level.append(curr.left.val)
                
                if curr.right:
                    q.append(curr.right) # 7
                    curr_level.append(curr.right.val)
            
            if len(curr_level)>0:
                out.append(curr_level)

        return out
