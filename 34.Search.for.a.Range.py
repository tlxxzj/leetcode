class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.binarySearchFirst(nums, target), self.binarySearchLast(nums, target)]
    
    def binarySearchFirst(self, nums, target):
        l, r, pos = 0, len(nums), -1
        while l < r:
            m = (l+r)/2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m
            else:
                pos = m
                r = m
        return pos
        
    def binarySearchLast(self, nums, target):
        l, r, pos = 0, len(nums), -1
        while l < r:
            m = (l+r)/2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m
            else:
                pos = m
                l = m + 1
        return pos
        