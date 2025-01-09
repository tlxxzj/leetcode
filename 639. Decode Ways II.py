class Solution:
    def numDecodings(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [0] * (n + 2)
        dp[-1] = dp[-2] = 1
        for i in range(n):
            if i > 0:
                c0 = s[i-1]
            else:
                c0 = ''
            c = s[i]
            if c >='1' and c <= '9':
                dp[i] += dp[i-1]
                if c0 == '1' or c0 == '*':
                    dp[i] += dp[i-2]
                if (c0 == '2' or c0 == '*') and c <= '6':
                    dp[i] += dp[i-2]
            elif c == '0':
                if c0 == '*':
                    dp[i] += dp[i-2] * 2
                elif c0 >= '1' and c0 <= '2':
                    dp[i] += dp[i-2]
                else:
                    return 0
            else:
                dp[i] += dp[i-1] * 9
                if c0 == '*':
                    dp[i] += 15 * dp[i-2]
                elif c0 == '1':
                    dp[i] += 9 * dp[i-2]
                elif c0 == '2':
                    dp[i] += 6 * dp[i-2]
            
            dp[i] %= mod
        #print(dp)
        return dp[n-1]