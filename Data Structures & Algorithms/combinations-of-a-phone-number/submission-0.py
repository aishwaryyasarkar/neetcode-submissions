class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        comb = []

        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return res

        def dfs(i):
            if i >= len(digits):
                res.append("".join(comb))
                return

            # choose a digit
            chars = digits_map[digits[i]]
            for c in chars:
                # choose a char
                comb.append(c)
                dfs(i+1)

                # undo
                comb.pop()
        dfs(0)
        return res
