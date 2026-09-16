class Solution:
    def jump(self, nums: List[int]) -> int:
        mem = {}

        def dfs(i):
            if i == len(nums) - 1:
                return 0

            if i >= len(nums):
                return float('inf')

            if i in mem:
                return mem[i]

            minSteps = float('inf')
            for j in range(nums[i]):
                minSteps = min(minSteps, dfs(i+j+1))

            mem[i] = minSteps + 1

            return minSteps + 1

        return dfs(0)

        