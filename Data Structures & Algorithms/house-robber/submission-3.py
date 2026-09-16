class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            return max(nums[0],nums[1])
        
        nums[-2] = max(nums[-1], nums[-2])
        
        for i in range(len(nums)-3, -1, -1):
            nums[i]=max(nums[i] + nums[i + 2], nums[i + 1])

        return max(nums[0],nums[1])