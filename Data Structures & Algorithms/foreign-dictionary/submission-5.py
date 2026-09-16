class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjHash = {}
        i, j = 0, 1

        for word in words:
            for ch in word:
                if ch not in adjHash:
                    adjHash[ch] = []

        while i < j and j <= len(words)-1:
            w1 = words[i]
            w2 = words[j]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    continue
                else:
                    adjHash[c1].append(c2)
                    break
            i+=1
            j+=1

        visited = set()
        path = set()
        res = ""

        def dfs(curr):
            nonlocal res

            if curr in path:
                return False   # cycle

            if curr in visited:
                return True
            
            path.add(curr) # visited = z, o
            if curr in adjHash:
                for nei in adjHash[curr]: # o
                    if not dfs(nei):
                        return False

            visited.add(curr)
            path.remove(curr)
            res = res + curr
            return True


        for nodes in adjHash:
            if not dfs(nodes): # z
                return ""

        return res[::-1]

