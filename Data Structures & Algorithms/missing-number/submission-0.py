class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) # 3

        for i, n in enumerate(nums):
            res = res ^ i
            res = res ^ n

        return res