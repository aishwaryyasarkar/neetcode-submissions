class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        i=0

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        while i <= len(s)-1:
            if s[i] not in pairs:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                opening_p = pairs[s[i]]
                if opening_p == stack[-1]:
                    stack.pop()
                else:
                    return False
            i+=1

        if not stack:
            return True

        return False

            