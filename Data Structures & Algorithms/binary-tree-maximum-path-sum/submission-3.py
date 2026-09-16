# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = float('-inf')
        
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            maxPath_children = 0

            # update max
            if left > 0:
                maxPath_children+=left

            if right > 0:
                maxPath_children+=right

            if maxPath_children > 0:
                self.maxPathSum = max(self.maxPathSum, maxPath_children+curr.val)
                return max(left,right)+curr.val
            else:
                self.maxPathSum = max(self.maxPathSum, curr.val)
                return curr.val
        
        dfs(root)

        return self.maxPathSum

        