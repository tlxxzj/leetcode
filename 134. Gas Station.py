class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        dp = [gas[i]-cost[i] for i in range(n)]
        if sum(dp) < 0:
            return -1
        ret = 0
        x = 0
        for i in range(n):
            x += dp[i]
            if x < 0:
                x = 0
                ret = i + 1
        return ret
