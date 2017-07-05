class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret=0
        i=0
        while i < len(nums):
            begin = i
            while i < len(nums) and nums[i] == 1:
                i += 1
            ret = max(ret, i-begin)
            while i < len(nums) and nums[i] == 0:
                i += 1
        return ret