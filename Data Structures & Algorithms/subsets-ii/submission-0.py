class Solution:
    """
    Subset I was:
    Given an array nums of unique integers, return all possible subsets of nums.
    The solution set must not contain duplicate subsets. You may return the solution in any order.
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # not include
            while (i+1) < len(nums) and nums[i+1] == nums[i]:
                 i+=1
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res