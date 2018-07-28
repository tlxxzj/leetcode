class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target):
            for num in nums:
                if num+i <= target:
                    dp[num+i] += dp[i]
        return dp[target]
        