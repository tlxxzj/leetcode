class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None : return 0
        if len(s) == 0: return 0
        if s[0] == '0': return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            if s[i] == '0':
                #error
                if s[i-1] != '1' and s[i-1] != '2':
                    return 0
                dp[i+1] = dp[i-1]
            else:
                dp[i+1] += dp[i]
                if i > 0 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                    dp[i+1] += dp[i-1]
        return dp[n]
