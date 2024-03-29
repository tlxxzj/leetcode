class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0
        n = len(s)
        dp = [0] *(n + 2)
        dp[-1] = dp[-2] = 1
        for i in range(n):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if i > 0 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
        return dp[i]