class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for price in prices:
            currProf = price - lowest
            lowest = min(lowest, price)
            profit = max(profit, currProf)
        return profit