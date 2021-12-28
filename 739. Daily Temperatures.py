class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n
        q = []
        for i in range(n):
            while len(q) > 0 and temperatures[q[-1]] < temperatures[i]:
                ret[q[-1]] = i - q[-1]
                q.pop()
            q.append(i)
        return ret
