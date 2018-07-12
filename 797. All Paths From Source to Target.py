class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def findPath(g, i, n, v, p, r):
            if i == n:
                r.append(p[:])
                return
            for j in g[i]:
                if not v[j]:
                    p.append(j)
                    v[j] = True
                    findPath(g, j, n, v, p, r)
                    p.pop()
                    v[j] = False
        
        n = len(graph) - 1
        v = [False] * (n + 1)
        p = []
        r = []
        
        p.append(0)
        v[0] = True
        findPath(graph, 0, n, v, p, r)
        
        return r