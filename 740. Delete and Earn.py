class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        points = defaultdict(int)
        for num in nums:
            points[num] += num
        
        nums = list(points.keys())
        nums.sort()
        n = len(nums)
        dp = [[0, 0] for i in range(n)]
        dp[0] = [0, points[nums[0]]]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            if nums[i-1] + 1 == nums[i]:
                dp[i][1] = dp[i-1][0] + points[nums[i]]
            else:
                dp[i][1] = dp[i][0] + points[nums[i]]
        
        return max(dp[-1])
