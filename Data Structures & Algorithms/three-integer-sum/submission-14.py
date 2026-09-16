class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        nums = sorted(nums)
        res = []

        # loop through a
        for idx, a in enumerate(nums):
            # handle duplicates, idx == idx -1
            if idx > 0 and a == nums[idx-1]:
                continue

            l,r = idx + 1, len(nums)-1
            # print(nums[l], nums[r])

            while l < r:
                # handle duplicates in sorted arr
                if (l>idx+1 and nums[l] == nums[l-1]):
                    l+=1
                    continue
                
                if (r<len(nums)-1 and nums[r] == nums[r+1]):
                    r-=1
                    continue

                if a + nums[l] + nums[r] == 0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1

                if a + nums[l] + nums[r] > 0:
                    r-=1
                
                if a + nums[l] + nums[r] < 0:
                    l+=1
        return res


