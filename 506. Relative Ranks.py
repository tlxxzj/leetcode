class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums2 = sorted(nums, reverse=True)
        top = {}
        for i in range(len(nums2)):
            top[nums2[i]] = i+1
        ret = []
        for i in nums:
            if top[i] == 1:
                ret.append('Gold Medal')
            elif top[i] == 2:
                ret.append('Silver Medal')
            elif top[i] == 3:
                ret.append('Bronze Medal')
            else:
                ret.append(str(top[i]))
        return ret
        