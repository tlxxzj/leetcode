class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        dp1 = A[0][:]
        dp2 = []
        for i in range(1, m):
            dp2 = [0] * n
            for j in range(1, n-1):
                dp2[j] = A[i][j] + min(dp1[j], dp1[j-1], dp1[j+1])
            if n > 1:
                dp2[0] = A[i][0] + min(dp1[0], dp1[1])
                dp2[n-1] = A[i][n-1] + min(dp1[n-1], dp1[n-2])
            else:
                dp2[0] = A[i][0] + dp1[0]
            #print(dp1, dp2)
            dp1 = dp2
        return min(dp1)