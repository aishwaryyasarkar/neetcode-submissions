class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        content = {}
        for s in strs:
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c) - ord('a')]+=1
            key = tuple(alphabet)
            if key not in content:
                content[key]=[]
            content[key].append(s)
            print(s, alphabet)
        return list(content.values())