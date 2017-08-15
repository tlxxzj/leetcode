class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        minx = 0
        maxx = 0
        if prices:
            minx=maxx=prices[0]
        i=0
        while i < len(prices):
            if prices[i] > maxx:
                maxx = prices[i]
            else:
                ret += maxx-minx
                maxx=minx=prices[i]
            i += 1
        ret += maxx-minx
        return ret