class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')

        def dfs(i, currentSum):
            nonlocal maxSum

            if i >= len(nums):
                return

            # considers 2 scenarios, sum until now and starting new from i
            currentSum = max(
                nums[i],
                currentSum + nums[i]
            )

            maxSum = max(maxSum, currentSum)

            dfs(i+1, currentSum)

        dfs(0, 0)
        return maxSum