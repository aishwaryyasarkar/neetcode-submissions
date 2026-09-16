class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        i=0

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            # add all opening to stack
            if c not in pairs:
                stack.append(c)
            else:
                # closing; if stack is empty, no opening, so False
                if not stack or  stack[-1] != pairs[c]:
                    return False

                stack.pop()
                # if stack:
                #     opening_p = pairs[c]
                #     if opening_p == stack[-1]:
                #         stack.pop()
                #     else:
                #         return False
                # else:
                #     return False

        if not stack:
            return True

        return False

            