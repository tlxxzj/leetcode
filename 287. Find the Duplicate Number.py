class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 1, n-1
        def count(p):
            lt, gt = 0, 0
            for i in nums:
                if i <= p:
                    lt += 1
                else:
                    gt += 1
            if lt>p:
                return -1
            else:
                return 1
        ret = l
        while l<=r:
            m = (l+r)/2
            k = count(m)
            if k<0:
                ret = m
                r = m-1
            else:
                l = m+1
                ret = m+1
        return ret
        
        