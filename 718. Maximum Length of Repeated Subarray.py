class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n1, n2 = len(A), len(B)
        dp = [[0]*(n2+1) for i in range(n1+1)]
        ret = 0
        for i in range(n1):
            for j in range(n2):
                if A[i] == B[j]:
                    dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j+1])
                    ret = max(ret, dp[i+1][j+1])
        
        return ret