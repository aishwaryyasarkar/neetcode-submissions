class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = len(text1)
        t2 = len(text2)

        mem = {}

        def dfs(i, j):
            if i == t1 or j == t2:
                return 0

            if (i, j) in mem:
                return mem[(i, j)]

            matches = 0

            if text1[i] == text2[j]:
                text1text2Match = dfs(i+1, j+1)
                matches = 1 + text1text2Match
            else:
                # skip from text 1
                text1Skip = dfs(i+1, j)

                # skip from text 2
                text2Skip = dfs(i, j+1)

                matches = max(text1Skip, text2Skip)

            mem[(i, j)] = matches

            return matches

        return dfs(0, 0)
