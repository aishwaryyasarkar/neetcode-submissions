class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            if n not in seen:
                seen[n]=1
            else:
                seen[n]+=1
        print(seen)
        return sorted(seen, key=lambda x: seen[x], reverse=True)[:k]