class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        """
        nums = nums=[3,4,5,6,1,2]  

        """
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            # left half sorted? and num between s and mid?
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
            
        return -1
