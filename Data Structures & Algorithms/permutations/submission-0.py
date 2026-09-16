class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for num in nums:
                if num in subset:
                    continue

                # include
                subset.append(num)
                dfs()

                # backtrack
                subset.pop()

        dfs()
        return res