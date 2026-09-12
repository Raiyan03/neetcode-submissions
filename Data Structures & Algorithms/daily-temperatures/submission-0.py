class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        for index, value in enumerate(temperatures):
            if index == n - 1:
                res.append(0)
                break
            count = 0
            found = False
            for i in range(index+1, n):
                count += 1
                if temperatures[i] > value:
                    found = True
                    break
            if found == True:
                res.append(count)
            else:
                res.append(0)
        return res
            