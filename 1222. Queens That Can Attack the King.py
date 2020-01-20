class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        board = [[False]*8 for i in range(8)]
        for r, c in queens:
            board[r][c] = True
        
        ret = []
        a, b = king[0], king[1]
        d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for x, y in d:
            for i in range(1, 8):
                r = a + x*i
                c = b + y*i
                if r < 0 or r > 7 or c < 0 or c > 7:
                    break
                if board[r][c]:
                    ret.append([r,c])
                    break
        return ret