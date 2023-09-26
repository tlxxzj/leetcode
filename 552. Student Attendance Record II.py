class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        A = 0
        L = 1
        LL = 2
        P = 3
        AL = 4
        ALL = 5
        AP = 6

        dp = [[0] * 7 for _ in range(n)]
        dp[0] = [1,1,0,1,0,0,0]

        for i in range(1, n):
            dp[i][A] = (dp[i-1][L] + dp[i-1][LL] +dp[i-1][P]) % MOD
            dp[i][L] = dp[i-1][P]
            dp[i][LL] = dp[i-1][L]
            dp[i][P] = (dp[i-1][L] + dp[i-1][LL] + dp[i-1][P]) % MOD

            dp[i][AL] = (dp[i-1][A] + dp[i-1][AP]) % MOD
            dp[i][ALL] = dp[i-1][AL]
            dp[i][AP] = (dp[i-1][A] + dp[i-1][AL] + dp[i-1][ALL] + dp[i-1][AP]) % MOD
        
        return sum(dp[n-1]) % MOD

