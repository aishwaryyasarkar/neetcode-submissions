class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return 0

        max_pile = max(piles)

        start, end = 1, max_pile
        k = max_pile
        while start <= end:
            mid = (start + end) // 2
            sum_p = 0
            for p in piles:
                sum_p+=math.ceil(p/mid)

            if sum_p>h:
                start=mid+1
            else:
                end=mid-1
                k=min(mid,k)
        return k
            
            