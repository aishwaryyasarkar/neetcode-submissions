class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1 = deque()
        stack2 = deque()

        for i, char in enumerate(s):
            if char == '*':
                stack2.append(i)
            elif char == '(':
                stack1.append(i)
            elif char == ')':
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False

        if stack1 and stack2:
            while stack1:
                if stack2:
                    if stack1.pop() > stack2.pop():
                        return False
                else:
                    return False
        
        if (not stack1 and stack2) or (not stack1 and not stack2):
            return True
        elif stack1 and not stack2:
            return False

                    


