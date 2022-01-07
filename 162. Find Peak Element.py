class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if i < n - 1 and nums[i] > nums[i+1]:
                return i
            if i == n -1 and nums[i] > nums[i-1]:
                return i
            i += 1
        return 0