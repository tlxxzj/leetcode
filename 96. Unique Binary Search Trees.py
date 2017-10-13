class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for k in range(2, n+1):
            for i in range(1, k+1):
                dp[k] += dp[i-1] * dp[k-i]
        return dp[n]
        