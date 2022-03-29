class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        m, k = 0, 0
        dp = [0] * n

        for i in range(n):
            if dp[i] > 0:
                continue
            s = set()
            j = i
            while not (j in s):
                s.add(j)
                j = nums[j]
            l = len(s) + dp[j]
            for x in s:
                dp[x] = l
        return max(dp)