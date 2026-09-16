class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = float('-inf')
        prevMin, prevMax = 1, 1
        for i in range(len(nums)):
            if i >= len(nums):
                return

            currMax = max(nums[i], nums[i]*prevMin, nums[i]*prevMax)
            currMin = min(nums[i], nums[i]*prevMin, nums[i]*prevMax)

            maxProduct = max(maxProduct, currMax)
            prevMin, prevMax = currMin, currMax    
        
        return maxProduct