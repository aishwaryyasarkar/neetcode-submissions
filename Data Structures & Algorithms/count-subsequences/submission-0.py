class Solution:
    """
    for every new char, either use or skip and see if it matches t before going out of bounds -- count every time it matches so return take + skip
    """
    def numDistinct(self, s: str, t: str) -> int:
        mem = {}

        def dfs(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0 # this means j has not reached the end but i has

            if (i, j) in mem:
                return mem[(i, j)]

            take, skip = 0, 0
            if s[i] == t[j]:
                # take curr
                take = dfs(i+1, j+1)

                # skip
                skip = dfs(i+1, j)
            else:
                skip = dfs(i+1, j)

            mem[(i, j)] = take + skip
            
            return take + skip

        return dfs(0, 0)