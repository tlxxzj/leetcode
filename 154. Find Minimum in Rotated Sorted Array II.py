class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) / 2
            x = nums[l]
            y = nums[r]
            z = nums[m]
            if x > y:
                if z >= x:
                    l = m + 1
                else:
                    l = l + 1
                    r = m
            elif x < y:
                r = m - 1
            else:
                l = l + 1
        return nums[l]
                
        