# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        def cmp(a, b):
            if a.start != b.start:
                return a.start-b.start
            return a.end-b.end
        
        def lower_bound(s, l, r, v):
            x=-1
            while l<=r:
                m = (l+r)/2
                if intervals[s[m]].start>=v:
                    r = m-1
                    x=m
                else:
                    l=m+1
            if x !=-1:
                x = s[x]
            return x
        
        n = len(intervals)
        st = range(n)
        st.sort(key=lambda x: intervals[x], cmp=cmp)
        ret = [-1] * n
        for i in xrange(n):
            ret[st[i]] = lower_bound(st, 0, n-1, intervals[st[i]].end)
        return ret
            
        