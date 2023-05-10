class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bits = [0] + [1<<i for i in range(9)]
        rows = [0] * 9
        cols = [0] * 9
        grids = [[0] * 3 for i in range(3)]

        for i in range(9*9):
            x, y = i // 9, i % 9
            digit = board[x][y]
            if digit == ".":
                continue
            
            digit = int(digit)
            bit = bits[digit]
            if rows[x] & bit > 0 or cols[y] & bit > 0 or grids[x//3][y//3] & bit > 0:
                return False
            rows[x] |= bit
            cols[y] |= bit
            grids[x//3][y//3] |= bit
        return True