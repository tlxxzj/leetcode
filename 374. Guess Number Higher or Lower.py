# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) >> 1
            k = guess(m)
            if k == -1:
                r = m - 1
            elif k == 1:
                l = m + 1
            else:
                return m
        return l