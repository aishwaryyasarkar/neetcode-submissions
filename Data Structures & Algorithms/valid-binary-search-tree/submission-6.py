# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, min_range, max_range):
            if not curr:
                return True

            current_valid = False

            if min_range < curr.val < max_range:
                  current_valid = True

            left_valid = dfs(curr.left, min_range, curr.val)
            right_valid = dfs(curr.right, curr.val, max_range)

            return (left_valid and right_valid and current_valid)

        return dfs(root, float('-inf'), float('inf'))