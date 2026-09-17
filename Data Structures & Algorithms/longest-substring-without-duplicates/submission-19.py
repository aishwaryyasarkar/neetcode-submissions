class Solution:
    """
    "zxyzxyz"
    l,r
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, right = 0, 0
        maxLength = 0
        while left <= right and right <= len(s) - 1:
            if s[right] not in charSet:
                charSet.add(s[right])
                right += 1
                maxLength = max(maxLength, right-left)
            else:
                # duplicate, should be squeezed until duplicate is removed
                charSet.remove(s[left])
                left+=1

        return maxLength
            