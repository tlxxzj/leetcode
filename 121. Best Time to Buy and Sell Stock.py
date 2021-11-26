class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        ret = 0
        for price in prices:
            minp = min(minp, price)
            ret = max(ret, price-minp)
        return ret