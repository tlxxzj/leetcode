class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        n, m = len(grid), len(grid[0])
        ret = 0
        island = lambda x, y: x>=0 and x<n and y>=0 and y<m and grid[x][y] == 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q = [[i, j]]
                    area = 0
                    while len(q) > 0:
                        area += 1
                        x, y = q.pop()
                        if island(x-1, y):
                            q.append([x-1, y])
                            grid[x-1][y] = 0
                        if island(x+1, y):
                            q.append([x+1, y])
                            grid[x+1][y] = 0
                        if island(x, y-1):
                            q.append([x, y-1])
                            grid[x][y-1] = 0
                        if island(x, y+1):
                            q.append([x, y+1])
                            grid[x][y+1] = 0
                    ret = max(ret, area)
        
        return ret