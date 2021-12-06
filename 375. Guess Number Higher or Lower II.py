class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[-1 for i in range(n+1)] for i in range(n+1)]
        def guess(i, j):
            if i == j:
                return 0
            if i + 1 == j:
                return i
            if dp[i][j] == -1:
                dp[i][j] = min([k + max(guess(i, k-1), guess(k+1, j)) for k in range(i+1, j)])
            return dp[i][j]
        
        return guess(1, n)

