class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx in range(len(nums)):
            find = target - nums[idx]
            if find not in seen:
                seen[nums[idx]]=idx
            else:
                return [seen[find],idx]