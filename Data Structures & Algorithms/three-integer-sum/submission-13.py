class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        out =[]
        nums_length = len(nums_sorted)

        for idx_a in range(nums_length):
            if nums_sorted[idx_a] == nums_sorted[idx_a-1] and idx_a>0:
                continue

            l = idx_a+1
            r = nums_length-1
            
                      
            while l < r:

                if l > idx_a+1 and r < nums_length-1:
                    if nums_sorted[l] == nums_sorted[l-1]:
                        l+=1
                        continue
                    
                    if nums_sorted[r] == nums_sorted[r+1]:
                        r-=1
                        continue

                # 2-sum
                if nums_sorted[idx_a]+nums_sorted[l]+nums_sorted[r]==0:
                    out.append([nums_sorted[idx_a],nums_sorted[l],nums_sorted[r]])
                    l+=1
                    r-=1

                if nums_sorted[idx_a]+nums_sorted[l]+nums_sorted[r]>0:
                    r-=1

                if nums_sorted[idx_a]+nums_sorted[l]+nums_sorted[r]<0:
                    l+=1

        return out