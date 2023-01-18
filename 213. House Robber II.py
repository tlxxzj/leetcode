class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for i in range(n)]
        dp2 = [[0, 0] for i in range(n)]
        dp2[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
            dp2[i][0] = max(dp2[i-1][0], dp2[i-1][1])
            if i != n - 1:
                dp2[i][1] = dp2[i-1][0] + nums[i]

        return max(*dp[-1], *dp2[-1])