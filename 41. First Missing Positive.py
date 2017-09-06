class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        n = len(nums)
        i = 0
        ret = n+1
        while i < n:
            e = nums[i]
            if i+1 != e and 1<= e <= n and nums[e-1] != e:
                nums[i], nums[e-1] = nums[e-1], e
            else:
                i += 1
        for i, e in enumerate(nums):
            if i+1 != e:
                return i+1
        return ret

