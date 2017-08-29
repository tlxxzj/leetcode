# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals

        def cmp(a, b):
            if a.start == b.start:
                return a.end-b.end
            return a.start-b.start
        
        def isoverlap(a, b):
            return a.end >= b.start
        
        intervals.sort(cmp=cmp)
        ret=[intervals[0]]
        k=0
        #return intervals
    
        for i in intervals[1:]:
            if isoverlap(ret[k], i):
                ret[k].end = max(i.end, ret[k].end)
            else:
                k += 1
                ret.append(i)
            
        return ret
