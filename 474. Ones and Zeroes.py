class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for i in xrange(m + 1)]
        for s in strs:
            z0 = sum(1 for c in s if c == '0')
            z1 = sum(1 for c in s if c == '1')
            for x in xrange(m, -1, -1):
                for y in xrange(n, -1, -1):
                    if x >= z0 and y >= z1:
                        dp[x][y] = max(dp[x][y], dp[x - z0][y - z1] + 1)        
        return dp[m][n]
