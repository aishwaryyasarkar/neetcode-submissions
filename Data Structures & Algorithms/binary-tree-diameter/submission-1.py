# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0

        # return height
        def dfs(curr):
            if not curr:
                return 0

            left_h = dfs(curr.left)
            right_h = dfs(curr.right)

            self.diam = max(self.diam, left_h + right_h)
            return max(left_h, right_h)+1

        dfs(root)
        return self.diam

