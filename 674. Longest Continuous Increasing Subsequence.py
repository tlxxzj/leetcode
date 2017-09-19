class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ret=0
        n = len(nums)
        k=1
        for i in range(1, n):
            if nums[i]>nums[i-1]:
                k +=1
                ret = max(ret, k)
            else:
                k = 1
        ret = max(ret, k)
        return ret
                