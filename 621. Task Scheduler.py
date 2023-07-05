class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = len(tasks)
        count = {}
        maxt = 0
        for t in tasks:
            count[t] = count.get(t, 0) + 1
            maxt = max(maxt, count[t])
        
        nt = 0
        for t in count.values():
            if t == maxt:
                nt += 1
        
        res = (maxt-1) * (n + 1) + nt
        res = max(res, m)
        return res

