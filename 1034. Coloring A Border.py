class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        color0 = grid[r0][c0]
        m, n = len(grid), len(grid[0])
        q = [(r0, c0)]
        vis = [[False]*n for i in range(m)]
        vis[r0][c0] = True
        border = []
        while len(q) > 0:
            x, y = q.pop()
            k = 0
            if x-1 >= 0 and grid[x-1][y] == color0:
                if not vis[x-1][y]: q.append((x-1, y))
                vis[x-1][y] = True
                k += 1
            if x+1 < m and grid[x+1][y] == color0:
                if not vis[x+1][y]: q.append((x+1, y))
                vis[x+1][y] = True
                k += 1
            if y-1 >= 0 and grid[x][y-1] == color0:
                if not vis[x][y-1]: q.append((x, y-1))
                vis[x][y-1] = True
                k += 1
            if y+1 < n and grid[x][y+1] == color0:
                if not vis[x][y+1]: q.append((x, y+1))
                vis[x][y+1] = True
                k += 1
            if k != 4:
                border.append((x, y))
        for x,y in border:
            grid[x][y] = color
            
        return grid
