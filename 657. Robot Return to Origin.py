class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l, u = 0, 0
        for m in moves:
            if m == 'L':
                l += 1
            elif m == 'R':
                l -= 1
            elif m == 'U':
                u += 1
            else:
                u -= 1
        
        return l == 0 and u == 0
