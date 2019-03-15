class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        d = {}
        inf = float('inf')
        for i in range(n):
            d[profit[i]] = min(d.get(profit[i], inf), difficulty[i])
        profit.sort()
        worker.sort(reverse=True)
        ret = 0
        p = n - 1
        for w in worker:
            while p >= 0 and w < d[profit[p]]:
                p -= 1
            if p >=                                                               0:
                ret += profit[p]
                
        return ret