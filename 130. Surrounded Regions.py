class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        visited = [[False for j in range(n)] for i in range(m)]
        q = []
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][n-1] == 'O':
                q.append((i, n-1))
        for j in range(n):
            if board[0][j] == 'O':
                q.append((0, j))
            if board[m-1][j] == 'O':
                q.append((m-1, j))
        while len(q) > 0:
            x,y=q.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            for i, j in [[0, 1],[1, 0],[0, -1],[-1, 0]]:
                x2 = x+i
                y2 = y+j
                if (0 <= x2 < m) and (0<= y2 < n) and (board[x2][y2] == 'O') and (not visited[x2][y2]):
                    q.append((x2, y2)) 

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if board[i][j] == 'O' and (not visited[i][j]):
                    board[i][j] = 'X'
        #return board


