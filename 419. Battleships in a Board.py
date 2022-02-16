class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ret = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                        ret += 1
        return ret