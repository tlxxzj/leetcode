class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(t.split(":")[0])*60+int(t.split(":")[1]) for t in  timePoints]
        timePoints.sort()
        print(timePoints)
        ret = min(timePoints[-1] - timePoints[0], timePoints[0] + 1440-timePoints[-1])
        for i in range(1, len(timePoints)):
            ret = min(ret, timePoints[i] - timePoints[i-1])
            ret = min(ret, timePoints[i-1] + 1440 - timePoints[i])
        return ret