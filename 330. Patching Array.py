class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m = len(nums)
        res = 0
        maxn = 1
        i = 0

        while maxn <= n:
            if i < m and nums[i] <= maxn:
                maxn += nums[i]
                i += 1
            else:
                maxn = maxn * 2
                res += 1
        
        return res
        
