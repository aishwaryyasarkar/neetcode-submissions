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
            # add all opening to stack
            if s[i] not in pairs:
                stack.append(s[i])
            else:
                # closing; if stack is empty, no opening, so False
                if stack:
                    opening_p = pairs[s[i]]
                    if opening_p == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            i+=1

        if not stack:
            return True

        return False

            