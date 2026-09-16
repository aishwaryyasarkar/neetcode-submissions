class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = {}
        
        def dfs(i):
            if i >= len(nums):
                return False
            
            if i == len(nums) - 1:
                return True

            if i in mem:
                return mem[i]

            reachedEnd = False
            for j in range(nums[i]):
                reachedEnd = reachedEnd or dfs(i+j+1)

            mem[i] = reachedEnd
            
            return reachedEnd
        
        return dfs(0)
