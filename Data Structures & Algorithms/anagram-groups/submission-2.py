from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_m = defaultdict(list)

        for idx, s in enumerate(strs):
            sorted_text = "".join(sorted(s))
            hash_m[sorted_text].append(s)
        
        return list(hash_m.values())
