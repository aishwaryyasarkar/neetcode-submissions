class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        zxyzxyz
        0123456
        l  r
        l   r
        as soon as a char is within l->r-1, save length
        """
        l, r = 0,0
        max_length = 1

        if not s:
            return 0

        length = 0
        """
            dvdf

        """
        while r<len(s):
            # keep pushing l till the point duplicate is removed
            while s[r] in s[l:r]:
                # max_length = max(max_length, length)
                l+=1
                length-=1
            length+=1
            max_length = max(max_length, length)
            r+=1
        
        return max_length





            



