class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i, n in enumerate(nums):
            if not count:
                count[n]=1
            else:
                if n in count:
                    count[n]+=1
                else:
                    count[n]=1
        print(count)
        res=sorted(count, key=count.get, reverse=True)
        print(res)
        return res[:k]