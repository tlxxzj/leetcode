class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        edges = [[] for i in range(N+1)]
        for u, v, w in times:
            edges[u].append((v, w))

        d = [-1] * (N + 1)
        d[0] = 0
        d[K] = 0

        q = []
        q.append((K, 0))
        while len(q) > 0:
            u, w = q.pop()
            if d[u] != -1 and d[u] < w:
                continue
            for v, w2 in edges[u]:
                w3 = w + w2
                if d[v] != -1 and d[v] <= w3:
                    continue
                d[v] = w3
                q.append((v, w3))

        minw, maxw = min(d), max(d)
        if minw == -1:
            return -1
        return maxw


