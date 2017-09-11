class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (not nums) or len(nums) < 3:
            return False
        ret = 1
        x = nums[0]
        y = float('inf')
        for i in nums:
            if i < x:
                x = i
            elif i > x and i < y:
                y = i
            if i > y:
                return True
        return False
            
            
            
        