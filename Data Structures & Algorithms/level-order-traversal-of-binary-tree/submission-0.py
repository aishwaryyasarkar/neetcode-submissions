# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
res = [[1],[2,3],]
queue = [4, 5, 6, 7]

0) add root to queue, add to res
0.1) while queue is not empty:
    0.2) run iteration till queue length at this moment, 2
        1) popleft() from q #1
        2) // if left or right is present, add to queue, add to res last list
4) return res
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()

        if not root:
            return []

        queue.append(root)
        res.append([root.val])
        """
        res = [[1], [2, 3], [4, 5, 6, 7]]
        queue = [4, 5, 6, 7]
        """
        while queue:
            current_res_size = len(res) # 3

            for i in range(len(queue)): # 4
                curr = queue.popleft()  

                if curr.left: # 
                    queue.append(curr.left) 
                    if len(res) == current_res_size:
                        res.append([curr.left.val])
                    else:
                        res[-1].append(curr.left.val)

                if curr.right: # 
                    queue.append(curr.right)
                    if len(res) == current_res_size:
                        res.append([curr.right.val])
                    else:
                        res[-1].append(curr.right.val)

        return res