class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        from functools import reduce
        def countN(x):
            if x == 0: return 1
            if x == 1: return 9
            return reduce(lambda x, y: x * (9-y), range(x-1), 9)
        return reduce(lambda x, y: x + countN(y), range(n+1), 0)
        