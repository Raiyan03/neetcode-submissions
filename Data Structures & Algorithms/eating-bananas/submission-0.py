class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r  = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for i in piles:
                totalTime += math.ceil(i/k)
            if totalTime <= h:
                res = k
                r = k - 1
            elif totalTime > h:
                l = k + 1
        return res