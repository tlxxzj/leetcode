class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >= 1 and n == n&(-n)