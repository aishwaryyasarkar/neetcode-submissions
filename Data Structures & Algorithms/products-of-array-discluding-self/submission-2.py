class Solution:
    """
    1, 2, 4, 6
    suffix = [1, 1, ]
    prod = 2 
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0 for i in range(len(nums))]
        suffix = [0 for i in range(len(nums))]

        prod = 1
        for i in range(len(nums)): # 1
            if i == 0:
                prefix[i] = prod
                continue

            prod *= nums[i-1]
            prefix[i]=prod

        prod = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                suffix[i]= prod
                continue
            prod *= nums[i+1]
            suffix[i]=prod

        return [x * y for x, y in zip(prefix, suffix)]
            

            