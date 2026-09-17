class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word = set(wordDict)
        mem = {}
        def dfs(i):
            if i == len(s): # when has gone out of bounds
                return True
            
            if i in mem:
                return mem[i]
            
            for j in range(i+1, len(s) + 1):
                if s[i:j] in word and dfs(j):
                    mem[i] = True
                    return True
            mem[i] = False
            return False

        return dfs(0)