class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.s = s
        for i in range(len(s)):
            # odd
            left, right = i, i
            self.isValidPalindrome(left, right)

            # even
            left, right = i, i+1
            self.isValidPalindrome(left, right)

        return self.res

    def isValidPalindrome(self, left, right):
        while left >= 0 and right <= len(self.s)-1 and self.s[left]==self.s[right]:
            if right - left +1 > len(self.res):
                self.res=self.s[left:right+1]
            left-=1
            right+=1