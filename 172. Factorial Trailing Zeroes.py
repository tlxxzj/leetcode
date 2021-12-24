class Solution:
    def trailingZeroes(self, n: int) -> int:
        ret = 0
        while n > 0:
            n = n // 5
            ret += n
        return ret