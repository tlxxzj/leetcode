class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        visited = [[False] * n for _ in range(m)]
        res = [[0] * n for _ in range(m)]
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    res[i][j] = -1
                else:
                    visited[i][j] = True
                    q.append((i,j))
        
        k = 0
        while len(q) > 0:
            q2 = []
            for x, y in q:
                if mat[x][y] == 1:
                    res[x][y] = k
                for dx, dy in moves:
                    x2, y2 = x+dx, y+dy
                    if x2<0 or x2>=m or y2<0 or y2>=n or visited[x2][y2]:
                        continue
                    visited[x2][y2] = True
                    q2.append((x2, y2))
            k += 1
            q = q2
        
        return res
