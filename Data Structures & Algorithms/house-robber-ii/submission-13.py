class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        if len(nums)==2:
            return max(nums[0],nums[1])
            
        temp = nums[:-1]
        nums = nums[1:]

        nums[-2] = max(nums[-1], nums[-2])
        temp[-2] = max(temp[-1], temp[-2])

        for i in range(len(nums)-3, -1, -1):
            nums[i]=max(nums[i] + nums[i + 2], nums[i + 1])

        for i in range(len(temp)-3, -1, -1):
            temp[i]=max(temp[i] + temp[i + 2], temp[i + 1])

        if len(nums)>1:
            return max(max(nums[0],nums[1]),max(temp[0],temp[1]))
        else:
            return max(nums[0],nums[1])
