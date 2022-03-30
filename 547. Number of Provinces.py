class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        e = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    e[i].append(j)
                    e[j].append(i)
        
        visited = [False] * n

        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for j in e[i]:
                dfs(j)
        ret = 0
        for i in range(n):
            if not visited[i]:
                ret += 1
                dfs(i)
        return ret