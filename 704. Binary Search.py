class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        if r < n and nums[r] == target:
            return r
        return -1