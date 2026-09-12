class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack = []
        for b in s:
            if b not in map:
                stack.append(b)
                continue
            if not stack or map[b] != stack[-1]:
                return False
            stack.pop()
        return not stack