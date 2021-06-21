class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        q = [[i] for i in range(1, n+1)]
        while len(q) > 0:
            q2 = []
            for comb in q:
                if len(comb) == k:
                    ret.append(comb)
                elif n - comb[-1] >= k - len(comb):
                    for i in range(comb[-1]+1, n+1):
                        comb2 = comb[:]
                        comb2.append(i)
                        q2.append(comb2)
            q = q2
        return ret