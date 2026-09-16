class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = len(t)
        have = 0
        haveHash = {}
        needHash = {}
        min_s = float('inf')
        res = ""
        
        for char in t:
            haveHash[char] = 0
            if char not in needHash:
                needHash[char] = 1
            else:
                needHash[char] += 1

        left, right = 0, 0
        while left<=right:
            if right >= len(s) and have < need:
                break
            if have < need:
                if s[right] in haveHash:
                    if haveHash[s[right]]<needHash[s[right]]:
                        have+=1
                    haveHash[s[right]]+=1
                right+=1
            elif have == need:
                if right-left < min_s:
                    min_s = right-left
                    res = s[left:right]

                if s[left] in haveHash:
                    if haveHash[s[left]]<=needHash[s[left]]:
                        have-=1
                    haveHash[s[left]]-=1
                left+=1
        return res



            

        
