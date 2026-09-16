class Solution:
    """
    1. if p has ., we can skip 1 char in a and p
    2. if p has *, 
        i. keep iterating in s until mismatch occurs or end of string
        ii. use * 0 times, meaning skip ?* completely.
    """
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            if (i, j) in mem:
                return mem[(i, j)]

            currMatch, use, skip = False, False, False
            # curr matching
            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                currMatch = True

            # next char
            if j+1 < len(p) and p[j+1] == "*":
                # use
                if currMatch:
                    use = dfs(i+1, j) # should break until mismatch or end of string
                
                # skip
                skip = dfs(i, j+2) # skip
                match = use or skip
            else:
                if currMatch:
                    match = dfs(i+1, j+1)
                else:
                    match = False   

            mem[(i, j)] = match
            return match       

        return dfs(0, 0)
        