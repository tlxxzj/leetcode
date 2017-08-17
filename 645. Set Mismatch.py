class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        ret=[0,0]
        while i < n:
            if i+1 == nums[i]:
                i+=1
                continue
            x=nums[i]
            if nums[x-1] == x:
                ret[0] = x
                ret[1] = i+1
                i+=1
                continue
            else:
                nums[i], nums[x-1] = nums[x-1], nums[i]
        return ret