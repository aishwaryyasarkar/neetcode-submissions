# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
left child < root
right child > root
at any point if this is false, return False, otherwise keep traversing

root = [2,1,3]
queue = [1]

1) add root to queue
2) while queue is not None:
3) pop queue 
4) if not left and if not right
4) check left and check right for validity, if both are valid, add both to queue
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()

        if not root:
            return None

        queue.append([root, float('-inf'), float('inf')])
        """
                    5
                   /\
                  4  6
                    / \
                   3   7
        root = [5,4,6, null, null, 3, 7]

        queue = []
        """
        while queue:
            curr, low, high = queue.popleft()

            if not (low < curr.val < high):
                return False

            if curr.left: 
                if curr.left.val >= curr.val:
                    return False
                else:
                    queue.append([curr.left, low, curr.val])

            if curr.right:
                if curr.right.val <= curr.val:
                    return False
                else:
                    queue.append([curr.right, curr.val, high])
        return True
            

        