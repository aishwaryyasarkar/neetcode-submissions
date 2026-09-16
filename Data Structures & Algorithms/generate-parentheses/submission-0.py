class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combinations = []
        opn, cls = 0, 0
        combinations.append("(")
        opn += 1

        def dfs(opn, cls):
            if opn == cls and opn == n and cls == n:
                res.append("".join(combinations))
                return

            # add open
            if opn < n:
                combinations.append("(")
                opn += 1
                dfs(opn, cls)

                # undo
                combinations.pop()
                opn -= 1

            # add clode
            if cls < opn and cls < n:
                combinations.append(")")
                cls += 1
                dfs(opn, cls)
                
                # undo
                combinations.pop()
                cls -= 1

        dfs(opn, cls)
        return res
