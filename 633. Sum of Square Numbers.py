class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import sqrt
        squares = set([i*i for i in range(int(sqrt(c))+1)])
        for square in squares:
            if c - square in squares:
                return True
        return False