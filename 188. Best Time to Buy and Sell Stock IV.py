class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        k = min(k, len(prices) // 2)
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for p in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1]-p)
                sell[i] = max(sell[i], buy[i]+p)

        return sell[k]
