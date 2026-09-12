class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0] * n
        stack = [] #[value, index]

        for i, value in enumerate(temperatures):
            while stack and stack[-1][0] < value:
                temp = stack.pop()
                out[temp[1]] = i - temp[1]
            stack.append([value, i])
        return out
                