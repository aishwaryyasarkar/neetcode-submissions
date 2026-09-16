# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = None
        # returns height
        def dfs(curr_p, curr_q):
            if not curr_p and not curr_q:
                return True

            if not curr_p or not curr_q:
                return False

            if curr_p.val != curr_q.val:
                return False

            left = dfs(curr_p.left, curr_q.left)
            right = dfs(curr_p.right,curr_q.right)

            return left and right

        return dfs(p, q)

            


            