class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        inf = float('inf')
        dp = [inf for i in xrange(n+1)]
        dp[0] = 0
        for i in xrange(n):
            j=1
            j2 = j*j+i
            while j2<=n:
                dp[j2] = min(dp[j2], dp[i]+1)
                j += 1
                j2 = j*j+i
        return dp[n]
        