class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        from collections import defaultdict
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                x = dp[j][diff]
                if x == 0:
                    dp[i][diff] += 1
                else:
                    dp[i][diff] += x + 1
                    res += x
        return res