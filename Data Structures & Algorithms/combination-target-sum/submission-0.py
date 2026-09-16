class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur_arr = []

        def dfs(i, total):
            if total == target:
                res.append(cur_arr.copy())
                return

            if i >= len(nums) or total > target:
                return

            cur_arr.append(nums[i]) # include ith element
            dfs(i, total + nums[i]) # continue

            cur_arr.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return res