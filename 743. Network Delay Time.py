class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge = [[] for i in range(n+1)]
        for u, v, w in times:
            edge[u].append((v, w))
        dp = [-1] * (n+1)
        dp[k] = 0
        q = [(k, 0)]
        while len(q) > 0:
            u, t = q.pop()
            for v, w in edge[u]:
                if dp[v] == -1 or t + w < dp[v]:
                    dp[v] = t + w
                    q.append((v, dp[v]))
        if dp.count(-1) > 1:
            return -1
        return max(dp[1:])

            