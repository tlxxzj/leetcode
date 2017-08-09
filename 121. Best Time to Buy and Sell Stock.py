class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        ret = 0
        if prices:
            minx = prices[0]
        for i in prices:
            ret = max(ret, i-minx)
            minx = min(minx, i)
        return ret
        
        