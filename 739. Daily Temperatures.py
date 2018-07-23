class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        waits = []
        ret = [0] * n
        for i, t in enumerate(temperatures, 0):
            while len(waits) > 0 and t > waits[-1][1]:
                ret[waits[-1][0]] = i - waits[-1][0]
                waits.pop()
            waits.append((i, t))
        return ret