class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        def lower_bound(l, r):
            while l <= r:
                m = (l + r) >> 1
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        def upper_bound(l, r):
            while l <= r:
                m = (l + r) >> 1
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        l = lower_bound(0, len(nums)-1)
        if l < len(nums) and nums[l] == target:
            return [l, upper_bound(l, len(nums)-1)-1]
        return [-1, -1]