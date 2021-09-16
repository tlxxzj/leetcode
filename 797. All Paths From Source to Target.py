class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)        
        ret = []
        path = [0] * n
        def dfs(i, p, q):
            path[i] = p
            if p == q:
                ret.append(path[:i+1])
                return
            for j in graph[p]:
                dfs(i+1, j, q)
        
        dfs(0, 0, n-1)

        return ret
