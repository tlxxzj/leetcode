class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        k = -1
        for num in nums:
            if num <= k:
                k += 1
                ret += k - num
            k = max(num, k)
        return ret