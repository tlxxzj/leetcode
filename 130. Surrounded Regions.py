class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(x, y):
            if x<0 or x>=m or y<0 or y>=n:
                return
            if board[x][y] != 'O':
                return
            board[x][y] = '.'
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
