class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        expected, actual = 0, 0
        for i, n in enumerate(nums):
            expected = expected ^ i
            actual = actual ^ n

        return expected ^ len(nums) ^ actual