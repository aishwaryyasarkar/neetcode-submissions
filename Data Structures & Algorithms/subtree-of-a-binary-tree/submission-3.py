# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False

        if not subRoot:
            return True

        if self.isSame(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))


        
    def isSame(self, r, sr):
        if not r and not sr:
            return True
        if (r and not sr) or (sr and not r):
            return False
        if r.val != sr.val:
            return False

        return self.isSame(r.left, sr.left) and self.isSame(r.right, sr.right)
        

