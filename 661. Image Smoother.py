class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0])
        
        def get(i, j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0, 0
            else:
                return 1, M[i][j]
            
        def avg(i, j):
            a, b = 0, 0
            for x, y in [[0, 0], [-1, -1], [-1, 0], [-1, 1], [1, 1], [1, 0], [1, -1], [0, -1], [0, 1]]:
                q, w = get(i+x, j+y)
                a+=q
                b+=w
            return b/a
            
        
        ret = [[avg(i, j) for j in xrange(n)] for i in xrange(m)]
        return ret
        