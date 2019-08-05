class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        
        dp = [[0]*(n2 + 1) for i in range(n1 + 1)]
        
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = max(dp[i][j] + 1, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
        
        return dp[n1][n2]