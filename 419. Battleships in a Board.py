class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        if m == 0:
            return 0
        n = len(board[0])
        if n == 0:
            return 0
        ret = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i-1 < 0 or board[i-1][j] != 'X') and (j-1 < 0 or board[i][j-1] != 'X'): 
                    ret += 1
        
        return ret
        