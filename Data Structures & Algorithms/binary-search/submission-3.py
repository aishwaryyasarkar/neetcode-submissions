class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        """ 2
               m
           -102468
            l     r
            6/2=3
        """

        while l <= r:
            print(l,r)
            mid = (l+r)//2
            
            if nums[mid] < target:
                l=mid+1
            elif nums[mid] > target:
                r=mid-1
            else:
                return mid
            

        return -1
            
