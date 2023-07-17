class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0
            if grid[x][y] == 0 or visited[x][y]:
                return 0
            visited[x][y] = True
            return dfs(x+1, y) + dfs(x-1, y) + dfs(x, y+1) + dfs(x, y-1) + 1

        for i in range(m):
            for j in range(n):
                area = dfs(i, j)
                res = max(res, area)
        
        return res