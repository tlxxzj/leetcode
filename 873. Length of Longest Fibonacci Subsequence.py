class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        set_a = set(A)
        n = len(A)
        dp = {}
        for a in A:
            dp[a] = {}
        ret = 0
        for i in range(1, n):
            z = A[i]
            for j in range(i-1, -1, -1):
                y = A[j]
                x = z - y
                if x >= y:
                    break
                if x in set_a:
                    dp[y][z] = max(dp[y].get(z, 0), dp[x].get(y, 2)+1)
                    ret = max(ret, dp[y][z])
        return ret
        
        