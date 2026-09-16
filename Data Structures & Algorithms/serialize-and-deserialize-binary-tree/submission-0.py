# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.tree = ""
        def dfs(curr):
            if not curr:
                self.tree = self.tree + "," + "N" if len(self.tree)>0 else self.tree + "N"
                return

            self.tree = self.tree + ","+ str(curr.val) if len(self.tree)>0 else self.tree + str(curr.val)

            dfs(curr.left)
            dfs(curr.right)

        dfs(root)
        return self.tree
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        values = data.split(",")

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
            

