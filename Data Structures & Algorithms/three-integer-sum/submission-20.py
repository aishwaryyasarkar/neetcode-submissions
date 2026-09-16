class Solution:
    """
    [-1,0,1,2,-1,-4]
    sort [-4, -1, -1, 0, 1, 2]
    first = -1
    -1 # sum = 1
    
    2
    res = [-1, -1, 2]
    1. sort
    2. Iterate through the array, as choose first
        i. target ?
        ii. left = i+1, right = len() - 1
        iii. if left + right > target: decrease right
        iv. else: increase left pointer
        v. left < right
        Note: must not repeat op on duplicates
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort
        res = []

        for i, first in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -first
            
            left = i+1
            right = len(nums) - 1

            """
            [-4, -1, -1, 0, 1, 2]
            """
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([first, nums[left], nums[right]])

                    # Move to new values
                    left += 1
                    right -= 1
                    
                    while left < right and right > 0 and nums[right] == nums[right+1]:
                        right -= 1
                    
                    while left < right and left < len(nums) - 1 and nums[left] == nums[left-1]:
                        left += 1

                elif nums[left] + nums[right] > target:
                    right -= 1

                    while left < right and right > 0 and nums[right] == nums[right+1]:
                        right -= 1
                else:
                    left += 1

                    while left < right and left < len(nums) - 1 and nums[left] == nums[left-1]:
                        left += 1
        return res 
                

