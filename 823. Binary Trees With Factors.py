class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        mod = 1000000000 + 7
        A.sort()
        n = len(A)
        d = {}
        x = {}
        for i in A:
            d[i] = 1
        for i in range(n):
            for j in range(i, n):
                p = A[i] * A[j]
                if p in d:
                    if p in x:
                        x[p].append((A[i], A[j]))
                    else:
                        x[p] = [(A[i], A[j])]
        for i in A:
            for a,b in x.get(i, []):
                c = d[a] * d[b]
                if a != b:
                    c *= 2
                d[i] = (d[i] + c) % mod
        return sum(d.values()) % mod
    