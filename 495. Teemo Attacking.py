class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        ret = 0
        x = timeSeries[0]
        for i in timeSeries:
            y = i + duration
            if y > x:
                ret += min(y - x, duration)
                x = y
        return ret
        