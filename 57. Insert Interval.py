# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        n = len(intervals)
        ret = []
        i = 0
        f = False
        while i < n:
            if (not f) and newInterval.start <= intervals[i].start:
                f = True
                start, end = newInterval.start, newInterval.end
                while i < n and intervals[i].start <= end:
                    end = max(end, intervals[i].end)
                    i += 1
                if ret and start <= ret[-1].end:
                    ret[-1].end = max(ret[-1].end, end)
                else:
                    ret.append(Interval(start, end))
            else:
                ret.append(intervals[i])
                i+=1
        if not f:
            if newInterval.start <= ret[-1].end:
                ret[-1].end = max(ret[-1].end, newInterval.end)
            else:
                ret.append(newInterval)
        return ret
        