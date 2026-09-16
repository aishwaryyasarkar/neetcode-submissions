class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # to include
            subset.append(candidates[i])
            dfs(i+1, total+candidates[i])

            # to not include
            subset.pop()
            
            # skip candidates[i] and all its duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i+1, total)

        dfs(0,0)

        return res
