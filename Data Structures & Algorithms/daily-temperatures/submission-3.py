class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for index, value in enumerate(temperatures):
            stack = []
            count = 0
            j = index + 1
            while len(stack) < 1 and j < len(temperatures):
                count += 1
                if value < temperatures[j]:
                    res.append(count)
                    stack.append(temperatures[j])
                else:
                    j += 1
            if len(stack) == 0:
                res.append(0)
        return res