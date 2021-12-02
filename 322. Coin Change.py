class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(amount+1-coin):
                dp[i+coin] = min(dp[i+coin], dp[i]+1)
        return dp[amount] if dp[amount] != float('inf') else -1