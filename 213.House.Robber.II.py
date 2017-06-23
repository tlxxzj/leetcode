class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=1:
            return self._rob(nums)
        else:
            return max(self._rob(nums[1:]), self._rob(nums[:-1]))
    
    def _rob(self, nums):
        n = len(nums)
        dp = [0] *(n+1)
        for i in range(1, n+1):
            if i == 1:
                dp[i] = nums[i-1]
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return dp[n]