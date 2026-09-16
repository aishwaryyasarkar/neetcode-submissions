class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        content_s = {}
        content_t = {}
        for idx, char in enumerate(s):
            if char not in content_s:
                content_s[char]=1
            else:
                content_s[char]+=1
        for idx, char in enumerate(t):
            if char not in content_t:
                content_t[char]=1
            else:
                content_t[char]+=1
        if content_s == content_t:
            return True
        return False