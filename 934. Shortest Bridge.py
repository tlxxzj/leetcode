class Que:
    def __init__(self):
        self.a = []
        self.b = []
    
    def push(self, x):
        self.b.append(x)

    def pop(self):
        if len(self.a) == 0:
            self.a = self.b
            self.a.reverse()
            self.b = []
        return self.a.pop()

    def size(self):
        return len(self.a) + len(self.b)

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def get_island(A, x, y, z):
            m, n = len(A), len(A[0])
            island = set()
            island.add((x, y))
            q = [(x, y)]
            A[x][y] = z
            while len(q) > 0:
                a, b = q.pop()
                if a + 1 < m and A[a+1][b] == 1 and (a+1, b) not in island:
                    island.add((a+1, b))
                    q.append((a+1, b))
                    A[a+1][b] = z
                if a - 1 >= 0 and A[a-1][b] == 1 and (a-1, b) not in island:
                    island.add((a-1, b))
                    q.append((a-1, b))
                    A[a-1][b] = z
                if b + 1 < n and A[a][b+1] == 1 and (a, b+1) not in island:
                    island.add((a, b+1))
                    q.append((a, b+1))
                    A[a][b+1] = z
                if b - 1 >= 0 and A[a][b-1] == 1 and (a, b-1) not in island:
                    island.add((a, b-1))
                    q.append((a, b - 1))
                    A[a][b-1] = z
            return island

        def get_bridge(A, x, y, z, ret, bridge):
            m, n = len(A), len(A[0])
            q = Que()
            q.push((x, y, 0))
            dx = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q.size() > 0:
                a, b, s = q.pop()
                if s - 1 > ret:
                    return ret
                if A[a][b] == z:
                    return s - 1
                for d in dx:
                    x2 = a + d[0]
                    y2 = b + d[1]
                    if x2 >= 0 and x2 < m and y2 >= 0 and y2 < n and A[x2][y2] in (0, z) and (bridge[x2][y2] == -1 or s + 1 < bridge[x2][y2]):
                        bridge[x2][y2] = s + 1
                        q.push((x2, y2, s+1))
            return float('inf')

        m, n = len(A), len(A[0])
        lands = []
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (len(lands) == 0 or (i, j) not in lands[0]):
                    land = get_island(A, i, j, len(lands)+1)
                    lands.append(land)
                    if len(lands) == 2:
                        break
        
        if len(lands[0]) > len(lands[1]):
            lands[0], lands[1] = lands[1], lands[0]

        bridge = [[-1 for i in range(n)] for j in range(m)]
        
        ret = float('inf')
        for x, y in lands[0]:
            z = 1
            if A[x][y] == 1:
                z = 2
            ret = min(ret, get_bridge(A, x, y, z, ret, bridge))
        
        return ret
        
