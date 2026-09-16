class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 0:
            return 0

        if len(nums) == 2:
            return max(nums[0], nums[1])

        def dp(nums: List[int]) -> int :
            for i in range(len(nums)-3, -1, -1):
                if i == len(nums)-3:
                    nums[i] += nums[i+2]
                else:
                    nums[i] += max(nums[i+2], nums[i+3])
            return max(nums[0], nums[1])


        return max(dp(nums[1:]), dp(nums[:-1]))