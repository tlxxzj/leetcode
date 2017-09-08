
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        n = len(M)
        p = [-1] * n
        ret = [n]
        def find(x):
            if p[x] == -1:
                return x
            else:
                y = find(p[x])
                p[x] = y
                return y
        
        def union(a, b):
            x = find(a)
            y = find(b)
            if x != y:
                p[y] = x
                ret[0] -= 1
        
        for i in xrange(n):
            for j in xrange(i, n):
                if M[i][j] == 1:
                    union(i, j)
                
        return ret[0]
        