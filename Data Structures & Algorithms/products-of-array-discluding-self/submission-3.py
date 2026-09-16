class Solution:
    """
    1, 2, 4, 6
    suffix = [1, 1, ]
    prod = 2 
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]

        prod = 1
        for i in range(len(nums)): # 1
            if i == 0:
                res[i] = prod
                continue

            prod *= nums[i-1]
            res[i]=prod

        prod = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                res[i] *= prod
                continue
            prod *= nums[i+1]
            res[i] *= prod

        return res
            

            