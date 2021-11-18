class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k <= 2: return k - 1
        from math import log
        return self.kthGrammar(n, k-(1<<int(log(k-1)/log(2)))) ^ 1