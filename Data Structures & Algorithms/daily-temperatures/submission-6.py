class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        out = [0] * n #[val, index]

        for i, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                temp = stack.pop()
                out[temp[1]] = i - temp[1]
            stack.append([val, i])
        return out