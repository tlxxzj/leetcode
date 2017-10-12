class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in coins:
            if i <= amount:
                dp[i] = 1
        for i in coins:
            for j in range(amount):
                if i + j <= amount and dp[j] > 0 and (dp[j] + 1 < dp[j + i] or dp[j + i] == -1):
                    dp[j + i] = dp[j] + 1
        #print dp
        return dp[amount]