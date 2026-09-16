class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        nums = [1,2,2,3,3,3], k = 2
        freqmap = [[1],_,_,_,_,_]
        """
        freqmap = [[] for _ in range(len(nums))] # ??
        count=0

        # sort
        nums.sort()

        for i in range(len(nums)): # n=2
            if i>0 and nums[i]!=nums[i-1]:
                # cal freq, add to freq
                freqmap[count-1].append(nums[i-1])
                count=0
            count+=1
            if i == len(nums)-1:
                freqmap[count-1].append(nums[i])

        """
        freqmap = [[1], [2], [3], [], [], []]
        res = []
        """
        res = []

        for f in range(len(freqmap)-1, -1, -1):
            for n in freqmap[f]:
                res.append(n)
                if len(res)==k:
                    return res

        return res

