class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_l = len(nums)
        start, end = 0, len(nums)-1
        res = -1

        while start <= end:
            mid = start + ((end-start)+1)//2
            # print(mid, nums[mid])

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1

            print(start, end)
        
        return res
