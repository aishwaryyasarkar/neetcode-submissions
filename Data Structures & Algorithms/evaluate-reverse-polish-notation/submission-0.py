class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": self.add,
            "-": self.sub,
            "*": self.mul,
            "/": self.div
        }

        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                one = stack.pop()
                two = stack.pop()
                stack.append(operators[s](two, one))
        
        return stack.pop()

    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return int(a/b)
    