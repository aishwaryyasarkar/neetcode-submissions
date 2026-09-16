# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = None
        # returns height
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            print(left, right, left-right)
            if left - right > 1 or left - right < -1:
                self.balanced = False

            return 1+max(left,right)
        
        dfs(root)
        print(self.balanced)
        if self.balanced==False:
            return self.balanced
        return True
        