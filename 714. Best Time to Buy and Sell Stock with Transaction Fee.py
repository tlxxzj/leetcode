class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = [0, -prices[0]]
        for p in prices:
            new_profit = [0, 0]
            new_profit[0] = max(profit[0], profit[1] + p - fee)
            new_profit[1] = max(profit[1], profit[0] - p)
            profit = new_profit
        
        return profit[0]


        
