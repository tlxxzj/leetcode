class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        LIVE = 0|2
        DIE = 1|4

        dx = [0, 0, -1, -1, -1, 1, 1, 1]
        dy = [-1, 1, 0, -1, 1, 0, -1, 1]
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                live = 0
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if board[x][y]&1 == 1:
                        live += 1
                
                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = DIE
                elif live == 3:
                    board[i][j] = LIVE
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == LIVE:
                    board[i][j] = 1
                elif board[i][j] == DIE:
                    board[i][j] = 0
        
                    
