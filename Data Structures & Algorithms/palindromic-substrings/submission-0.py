class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        self.s = s

        for center in range(len(s)):
            # odd
            left, right = center, center
            self.isPalindrome(left, right)

            # even
            left, right = center, center + 1
            self.isPalindrome(left, right)

        return self.count

    def isPalindrome(self, left, right):
        while left >= 0 and right <= len(self.s)-1 and self.s[left]==self.s[right]:
            self.count += 1
            left -= 1
            right += 1
