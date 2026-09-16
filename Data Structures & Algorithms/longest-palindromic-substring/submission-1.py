class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd
            left, right = i, i
            while left >= 0 and right <= len(s)-1 and s[left]==s[right]:
                if right - left +1 > len(res):
                    res=s[left:right+1]
                left-=1
                right+=1

            # even
            left, right = i, i+1
            while left >= 0 and right <= len(s)-1 and s[left]==s[right]:
                if right - left +1 > len(res):
                    res=s[left:right+1]
                left-=1
                right+=1

        return res