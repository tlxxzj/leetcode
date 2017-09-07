class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0
        def cmp(a, b):
            if a[0] != b[0]:
                return a[0]-b[0]
            return a[1]-b[1]
        pairs.sort(cmp=cmp)
        n = len(pairs)
        dp = [1] * n
        for i in xrange(n):
            for j in xrange(i):
                if pairs[j][1] < pairs[i][0] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
        return max(dp)
        