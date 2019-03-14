class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dyas = set(days)
        dp = [float('inf')] * (366 + 30)
        dp[0] = 0
        for i in range(1, 366):
            if i in days:
                dp[i] = min(dp[i], dp[i-1] + costs[0])
                for j in range(7):
                    dp[i+j] = min(dp[i+j], dp[i-1] + costs[1])
                for j in range(30):
                    dp[i+j] = min(dp[i+j], dp[i-1] + costs[2])
            else:
                dp[i] = min(dp[i], dp[i-1])
        
        #print(dp[:max(days)])
        return dp[max(days)]