class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_length = len(s)
        left, right = 0, 1
        max_l=0
        l = 1

        if s_length == 0:
            return 0
        
        if s_length == 1:
            return 1

        while right <= s_length -1:
            # print(s[left:right], max_l, left, right)
            
            if s[right] in s[left:right]:
                left+=1
                l-=1
            else:
                right+=1
                l+=1
            if l > max_l:
                max_l=l
        return max_l

            



