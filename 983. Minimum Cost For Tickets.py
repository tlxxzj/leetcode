class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float('inf')] * (n + 1)
        dp[-1] = 0
        for i in range(n):
            #costs[0]
            dp[i] = min(dp[i], dp[i-1] + costs[0])
            #costs[1]
            j = i
            while j < n and days[j] - days[i] < 7:
                dp[j] = min(dp[j], dp[i-1] + costs[1])
                j += 1
            #cost[2]
            j = i
            while j < n and days[j] - days[i] < 30:
                dp[j] = min(dp[j], dp[i-1] + costs[2])
                j += 1
        #print(dp)
        return dp[n-1]

                