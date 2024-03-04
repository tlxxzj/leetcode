class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [-float('inf')] * 3
        sell = [0] * 3
        for p in prices:
            for i in range(1, 3):
                buy[i] = max(buy[i], sell[i-1]-p)
                sell[i] = max(sell[i], buy[i]+p)
        return sell[2]
