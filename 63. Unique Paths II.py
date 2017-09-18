class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        g = obstacleGrid
        m = len(g)
        n = len(g[0])
        if g[0][0] == 1 or g[-1][-1] == 1:
            return 0
        ret = [[0 for j in xrange(n)] for i in xrange(m)]
        ret[0][0] = 1
        for i in xrange(m):
            for j in xrange(n):
                if (g[i][j] == 0) and (i>0 or j>0):
                    x= ret[i-1][j] if i>0 else 0
                    y= ret[i][j-1] if j>0 else 0
                    ret[i][j] = x + y
        
        return ret[-1][-1]
        
        