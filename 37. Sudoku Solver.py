class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        grid = [[set() for j in range(3)] for i in range(3)]
        si = [str(i) for i in range(10)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                x = int(board[i][j])
                row[i].add(x)
                col[j].add(x)
                grid[i/3][j/3].add(x)
        
        def solve(k):
            if k == 81:
                return True
            x, y = k/9, k%9
            if board[x][y] != '.':
                return solve(k+1)
            for i in range(1, 10):
                if (i in row[x]) or (i in col[y]) or (i in grid[x/3][y/3]):
                    continue
                row[x].add(i)
                col[y].add(i)
                grid[x/3][y/3].add(i)
                board[x][y] = si[i]
                if solve(k+1):
                    return True
                row[x].remove(i)
                col[y].remove(i)
                grid[x/3][y/3].remove(i)
                board[x][y] = '.'
            return False
        
        solve(0)
        