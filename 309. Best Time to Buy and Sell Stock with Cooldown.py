class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0

        dp = [[0]*3 for i in range(n)]
        dp[0][0] = -prices[0]
        
        maxprofit = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][2] - prices[i], dp[i-1][0])
            dp[i][1] = max(prices[i] + dp[i-1][0], dp[i-1][1])
            dp[i][2] = dp[i-1][1]
            maxprofit = max(maxprofit, dp[i][1])
        return maxprofit
