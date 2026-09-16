class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            prev = target - nums[i]
            if prev in visited:
                return [visited[prev], i]
            visited[nums[i]] = i

        return -1