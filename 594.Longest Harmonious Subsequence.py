class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        ret = 0
        for k, v in d.iteritems():
            if k-1 in d:
                ret = max(ret, v+d[k-1])
            if k+1 in d:
                ret = max(ret, v+d[k+1])
        return ret
        