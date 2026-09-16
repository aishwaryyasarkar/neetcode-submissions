class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            [1,2,4,6]
            [1,1,1,1]
            prefix
              1: 
              2: 1
              4: 1*2
              6: 1*2*4
            suffix
              1: 6*4*2
              2: 6*4
              4: 6
              6: 
            O(n) so loop cannot be nested
        """
        res = [1]*len(nums)
        prefix, suffix = 1, 1
        # prefix
        for idx, n in enumerate(nums):
            if idx==0:
                continue
            prefix*=nums[idx-1]
            res[idx] = prefix

        
        # suffix
        for idx in reversed(range(len(nums))):
            if idx==len(nums)-1:
                continue
            suffix*=nums[idx+1]
            res[idx]*= suffix
        
        return res

