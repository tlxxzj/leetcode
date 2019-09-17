class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(d):
            for j in range(target, i, -1):
                dp[j] = 0
                for k in range(1, f+1):
                    if j-k >=i:
                        dp[j] += dp[j-k]
                        dp[j] %= 1000000007
        return dp[target]
                