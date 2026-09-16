class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
           1,2,2,3,3,3

           1    2   3   4   5   6
           [1] [2] [3]
        """
        # Each frequency must hold a list because
        # multiple numbers can have the same frequency.
        count_val = [[] for _ in range(len(nums))]
        
        # if not sorted, we need to sort it
        nums = sorted(nums)

        c = 0
        for i in range(len(nums)):
            if i>0 and nums[i]!=nums[i-1]:
                count_val[c-1].append(nums[i-1])
                c = 0
            c+=1
            if i == len(nums)-1:
                count_val[c-1].append(nums[i])

        res = []
        j = len(count_val) - 1

        while j >= 0 and len(res)<=k:
            for number in count_val[j]:
                res.append(number)

                if len(res) == k:
                    return res
            j-=1
        return res