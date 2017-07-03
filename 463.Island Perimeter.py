class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m,n = len(grid), len(grid[0])
        ret = 0
        def isEdge(i, j):
            if i<0 or i >=m or j<0 or j>=n or grid[i][j] ==0:
                return 1
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ret += isEdge(i+1, j) + isEdge(i-1, j) + isEdge(i, j+1) + isEdge(i, j-1)
        return ret
        
        
        
        