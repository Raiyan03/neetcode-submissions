class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openB, ClosedB):
            if openB == ClosedB == n:
                res.append("".join(stack))
                return
            if openB < n:
                stack.append("(")
                backtrack(openB + 1, ClosedB)
                stack.pop()
            if ClosedB < openB:
                stack.append(")")
                backtrack(openB, ClosedB + 1)
                stack.pop()
        backtrack(0, 0)
        return res