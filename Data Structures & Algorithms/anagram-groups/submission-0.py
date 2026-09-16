class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i, s in enumerate(strs):
            print(i, s)
            if not seen:
                seen["".join(sorted(s))]=[s]
            else:
                curr = "".join(sorted(s))
                if curr in seen:
                    seen[curr].append(s)
                else:
                    seen[curr]=[s]
        return list(seen.values())