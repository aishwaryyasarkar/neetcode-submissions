# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        depth_left, depth_right = 0,0 
        
        def dfs(root):
            if not root:
                return 0

            depth_left = dfs(root.left)
            depth_right = dfs(root.right)

            self.diameter = max(self.diameter, depth_left + depth_right)

            return 1+max(depth_left, depth_right)

        dfs(root)
        return self.diameter
