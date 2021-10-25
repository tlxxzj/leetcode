class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        i, j = 0, 0
        while j < n:
            k = 1
            v = nums[j]
            j += 1
            while j < n and nums[j] == v:
                j += 1
                k += 1
            k = min(2, k)
            while k > 0:
                nums[i] = v
                i += 1
                k -= 1
        return i