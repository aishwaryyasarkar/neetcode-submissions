class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        counts = Counter(nums)
        print(counts)
        for count in counts.values():
            if count > 1:
                return True
        return False