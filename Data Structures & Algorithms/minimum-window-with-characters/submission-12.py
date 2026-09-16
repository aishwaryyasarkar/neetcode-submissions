class Solution:
    """
    Input: s = "OUZODYXAZV", t = "XYZ" # lengths = 4

    Output: "YXAZ"

    Hash = {
    X: 1
    Y: 1
    Z: 1
    }

    """
    def minWindow(self, s: str, t: str) -> str:
        needHash = {}
        haveHash = {}
        need = len(t)
        have = 0

        res = ""
        minLen = float('inf')

        for c in t:
            if c not in needHash:
                needHash[c] = 0
                haveHash[c] = 0
            needHash[c]+=1

        left, right = 0, 0

        while left <= right:
            if right >= len(s) and have < need:
                break
            
            if have < need:
                if s[right] in needHash:
                    if haveHash[s[right]] < needHash[s[right]]:
                        have += 1
                    haveHash[s[right]] += 1 # this always increases, but have variable only increases when total have < total need
                right += 1
            elif have == need:
                if right - left < minLen:
                    minLen = right - left
                    res = s[left:right] # right has already on the next
                
                if s[left] in needHash:
                    if haveHash[s[left]] <= needHash[s[left]]:
                        have -= 1
                    haveHash[s[left]] -= 1
                left += 1
        return res
            
            
            





        
        