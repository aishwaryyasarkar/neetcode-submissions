# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Input: root = [2,1,1,3,null,1,5]
> goodNodes(2), good, count = 1 --> returns 3
- > goodNodes(1) - max=2
- - > goodNodes(3) - max=2 3>=2, good, return count += 1; 2

- > goodNodes(1), not good, max = 2 
- - > goodNodes(1), not good, max = 2
- - > goodNodes(5), good, max=2, 5>=2, return count+= 1; 3

> goodNodes(2), good, count = 1, max = 2, 
- > left: goodNodes(1, max=2) - not good, count = 1, max = 2
- - > left: goodNodes(3) - good, count = 2, max = 3, return 2
- - > right: goodNodes(None) - return 2

- > right: goodNodes(1, max=2), not good, max = 2
- - > left: goodNodes(1, max=2), not good, max = 2 
- - > right: goodNodes(5, max=3), good, max = 5, count=3, return 3 

"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # count = 0 # 1
        self.max_soFar = root.val

        def dfs(curr, max_soFar): 
            if not curr:
                return 0

            max_soFar = max(max_soFar, curr.val) 

            left_count = dfs(curr.left, max_soFar) # returns 2
            right_count = dfs(curr.right, max_soFar)

            if curr.val >= max_soFar:
                return (left_count+right_count)+1
            else:
                return left_count+right_count
        
        return dfs(root, self.max_soFar)
        