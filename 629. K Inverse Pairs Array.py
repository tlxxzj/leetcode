class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k+1) for i in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n):
            dp[i][0] = 1
            for j in range(1, k+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                if j > i:
                    dp[i][j] -= dp[i-1][j-i-1]
                dp[i][j] %= MOD
        
        return dp[n-1][k]
