class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ret = 0
        end = 0
        for t in timeSeries:
            ret += duration
            ret -= max(0, end - t)
            end = t + duration
        return ret
