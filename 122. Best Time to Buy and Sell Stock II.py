class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        p = prices[0]
        for price in prices:
            if price > p:
                ret += price - p
            p = price
        return ret