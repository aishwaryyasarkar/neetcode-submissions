class Solution:
    """
    # add

    # sub
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}

        def dfs(i, amt):
            if i >= len(nums):
                if amt == target:
                    return 1
                return 0

            if (i, amt) in mem:
                return mem[(i, amt)]

            # add
            add = dfs(i+1, amt+nums[i])

            # sub
            sub = dfs(i+1, amt-nums[i])

            mem[(i, amt)] = add + sub

            return add + sub

        return dfs(0, 0)