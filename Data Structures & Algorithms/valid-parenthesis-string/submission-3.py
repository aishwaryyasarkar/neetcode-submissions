class Solution:
    """
    *)*
    
    """
    def checkValidString(self, s: str) -> bool:
        stack1 = deque() # for opening brackets
        stack2 = deque() # for *

        for i, c in enumerate(s):
            if c == "(":
                stack1.append(i)
            
            if c == "*":
                stack2.append(i)
            
            if c == ")":
                if stack1:
                    stack1.pop()
                elif stack2: # use a *
                    stack2.pop()
                else:
                    return False

        if len(stack1) > len(stack2):
            return False
        else:
            while stack1:
                i = stack1.pop()
                j = stack2.pop()

                if j < i:
                    return False
            return True

        

                    


