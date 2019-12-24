from functools import cmp_to_key
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def cmp(a, b):
            if a[0] == b[0]:
                return b[1] - a[1]
            return a[0] - b[0]
        intervals.sort(key=cmp_to_key(cmp))
        ret = 1
        maxb = intervals[0][1]
        for interval in intervals:
            if interval[1] <= maxb:
                continue
            else:
                maxb = interval[1]
                ret+=1
        return ret
