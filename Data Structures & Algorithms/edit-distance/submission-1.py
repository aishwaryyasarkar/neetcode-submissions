class Solution:
    """
    Iterate together and keep matching..
    When there is a mismatch, we have 3 options..
    1. Remove:
        i. when next char in word1 gives the match, then we can remove current, and count this as 1 op performed
        ii. if word1 has extra char and we already matched with word2
    2. Replace:
        i. when next char in word1 is a mismatch, then we replace curr with what whats in word2
    3. 
    """
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        
        def dfs(i, j):
            if j == len(word2):
                return len(word1) - i # this many needs to be removed

            if i == len(word1):
                return len(word2) - j # this many needs to be inserted

            if (i, j) in mem:
                return mem[(i, j)]

            if word1[i] != word2[j]:
                # Insert
                insert = dfs(i, j+1)

                # Remove
                remove = dfs(i+1, j)

                # Replace
                replace = dfs(i+1, j+1)

                res = 1 + min(insert, remove, replace)
            else:
                res = dfs(i+1, j+1)
            
            mem[(i, j)] = res
            return res 

        return dfs(0,0)