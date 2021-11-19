class Solution:
    def integerReplacement(self, n: int) -> int:
        if n <= 1:
            return 0
        if n & 1 == 0:
            return self.integerReplacement(n>>1) + 1
        else:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))