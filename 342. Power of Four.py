class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n == 1 or (n > 0 and -n&n == n and n%10 in [4, 6])