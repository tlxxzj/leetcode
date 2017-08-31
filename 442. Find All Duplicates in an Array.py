class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = set()
        n=len(nums)
        i=0
        while i < n:
            x = nums[i]
            if i+1 == x:
                i += 1
                continue
            if nums[x-1] == x:
                i += 1
                ret.add(x)
                continue
            nums[x-1], nums[i] = x, nums[x-1]
        return list(ret)
