class Solution:
    """
    substrings should have unique letters as each letter can appear in at most one substring
    """
    def partitionLabels(self, s: str) -> List[int]:
        lastIdxMap = {}

        for i, c in enumerate(s):
            if c not in lastIdxMap:
                lastIdxMap[c] = 0
            lastIdxMap[c] = i

        lastSeen = -1
        res = []
        count = 0

        for i, c in enumerate(s):
            count+=1

            if c in lastIdxMap:
                lastSeen = max(lastSeen, lastIdxMap[c])

            if i == lastSeen:
                res.append(count)
                count = 0
        return res
                
            