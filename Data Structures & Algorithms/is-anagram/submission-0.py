class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            hash_s=Counter(s)
            hash_t=Counter(t)
            for k in hash_s:
                if hash_t[k] == hash_s[k]:
                    continue
                else:
                    return False
            return True
        else:
            return False