class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            elif i == '+':
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif i == '*':
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif i == '-':
                a, b = stack.pop(), stack.pop()
                val = b - a
                stack.append(val)
            elif i == '/':
                a, b = stack.pop(), stack.pop()
                val = int(b / a)
                stack.append(val)
        return stack.pop()