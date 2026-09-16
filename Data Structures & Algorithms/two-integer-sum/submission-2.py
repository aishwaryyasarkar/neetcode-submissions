class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0,1

        hash_m = {}
        
        for idx, n in enumerate(nums):
            if target - n not in hash_m:
                hash_m[n]=idx
            else:
                return [hash_m[target-n],idx]

        return 0