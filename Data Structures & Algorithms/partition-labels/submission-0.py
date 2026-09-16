class Solution:
    """
    substrings should have unique letters as each letter can appear in at most one substring
    """
    def partitionLabels(self, s: str) -> List[int]:
        endMap = {}

        for i, v in enumerate(s):
            if v not in endMap:
                endMap[v] = 0
            endMap[v] = i
        
        res = []

        count = 0
        lastidxPartition = 0
        for i in range(len(s)):
            char = s[i]
            count += 1

            lastidxPartition = max(lastidxPartition, endMap[char])

            if lastidxPartition == i:
                res.append(count)
                count = 0

        return res
