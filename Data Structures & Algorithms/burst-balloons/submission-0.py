class Solution:
    """
    all needs to be burst, so we start w left most 
    if we are bursting current balloon, check i - 1 and i + 1, if there are oob, then use 1 as value.. coins you get is int of curr * prev * next

    """
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        mem = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in mem:
                return mem[(l, r)]

            mem[(l, r)] = 0

            for i in range(l, r + 1): # l through r, since python range takes r+1
                coins = nums[l-1] * nums[i] * nums[r+1] # i is last, so l-1 and r+1
                coins += dfs(l, i-1) + dfs(i+1, r)
                mem[(l, r)] = max(mem[(l, r)], coins)
            return mem[(l, r)]

        return dfs(1, len(nums) - 2)