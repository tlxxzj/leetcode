class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        dp = [0]*n
        for i in range(0, n-1):
            for j in range(i+1, n):
                if prices[j] > prices[i]:
                    x = dp[i-2] if i-2>=0 else 0
                    dp[j] = max(dp[j], x+prices[j]-prices[i])
                else:
                    dp[j] = max(dp[j], dp[j-1])
        return dp[n-1]

