class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        inf = float('inf')
        dp = [[inf] * (i+1) for i in range(n+1)]
        dp[1][0] = 0
        dp[1][1] = 1
        for i in range(1, n):
            for j in range(1, i):
                if dp[i][j] == inf:
                    continue
                if i+j <= n:
                    dp[i+j][j] = min(dp[i+j], dp[i][j]+1)
            if i+i <= n:
                dp[i+i][i] = min(dp[i+i][i+i], min(dp[i])+2)
        
        return min(dp[n])