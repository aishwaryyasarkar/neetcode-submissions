class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) < 1:
            return 0
            
        for i in range(len(nums)-3, -1, -1):
            if i == len(nums)-3:
                nums[i] = nums[i] + nums[i+2]
            else:
                nums[i] = nums[i] + max(nums[i+2], nums[i+3])

        return max(nums[0], nums[1])