class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def neighbors(x, y):
            cnt = 0
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                x2, y2 = x+dx, y+dy
                if x2>=0 and x2<m and y2>=0 and y2<n and grid[x2][y2] == 1:
                    cnt += 1
            return cnt

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                res += 4 - neighbors(i, j)
        
        return res
