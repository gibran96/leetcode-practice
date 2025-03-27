class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["+", "-", "*", "/"]
        stack = []
        for t in tokens:
            if t in op:
                print(t)
                b = int(stack.pop())
                a = int(stack.pop())
                if t == "+": stack.append(str(a + b))
                if t == "-": stack.append(str(a - b))
                if t == "*": stack.append(str(a * b))
                if t == "/": stack.append(str(int(a / b)))
            else:
                stack.append(t)
        return int(stack.pop())