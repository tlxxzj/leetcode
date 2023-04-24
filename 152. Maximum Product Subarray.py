class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for i in range(n+1)]
        dp[-1][0] = dp[-1][1] = 1
        ret = nums[0]
        for i in range(n):
            dp[i][0] = max(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])
            dp[i][1] = min(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])
            ret = max(ret, dp[i][0], dp[i][1])
        return ret
