class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l + r) >> 1
            '''
            if nums[m] > nums[m+1] then peak element exists in [l,m]
            if nums[m] < nums[m+1] then peak element exists in [m+1,r]
            '''
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1
        return l