class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
           2,20,4,10,3,4,5 
           s, s,  ,s,     
           2,20,4,10,3,5
        """
        myset = set(nums)
        max_l=0
        l=1

        for n in myset:
            if n-1 not in myset:
                curr = n
                while curr+1 in myset:
                    l+=1
                    curr+=1
            max_l=max(max_l,l)
            l=1
        
        return max_l
