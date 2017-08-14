# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r,ret=1,n,1
        while l<=r:
            m=(l+r)/2
            if isBadVersion(m):
                r=m-1
                ret=m
            else:
                l=m+1
        return ret
        
        