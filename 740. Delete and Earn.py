class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.append(0)
        maxn = max(nums)
        arr = [0] * (maxn + 1)
        for i in nums:
            arr[i] += 1
        
        dp = [[0, 0] for i in range(maxn + 1)]
        ret = 0
        for i in range(1, maxn + 1):
            #pick i
            dp[i][1] = dp[i-1][0] + i * arr[i]
            
            #else
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            
            ret = max(dp[i][0], dp[i][1])
        
        return ret
            