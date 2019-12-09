class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [{} for i in range(n)]
        ret = 0
        for i in range(0, n):
            for j in range(i+1, n):
                x = A[j] - A[i]
                y = max(dp[j].get(x, 1), dp[i].get(x, 1) + 1)
                ret = max(ret, y)
                dp[j][x] = y
        return ret