class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p = 1
        n = len(nums)
        j = -1
        ret = 0
        for i in range(n):
            p *= nums[i]
            while p >= k and j < i:
                j += 1
                p /= nums[j]
            if p < k:
                ret += i - j
        return ret