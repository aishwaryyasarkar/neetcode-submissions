# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
root = [8,4,12,2,6,10,14]

left > dfs(4) > dfs(2) [k=1] > dfs(None) [k=0]
curr > dfs(8) > dfs(4)
right > dfs(12) >
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.out = 0
        self.count = 0

        def dfs(curr):
            if not curr:
                return 0

            dfs(curr.left)

            self.count+=1
            if self.count == k:
                self.out = curr.val

            dfs(curr.right)

        dfs(root)
        
        return self.out