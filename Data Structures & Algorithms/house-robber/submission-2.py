class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums)-3, -1, -1):
            nums[i]=max(nums[i] + nums[i + 2], nums[i + 1])

        if len(nums)>1:
            return max(nums[0],nums[1])
        else:
            return nums[0]