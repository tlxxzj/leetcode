class Solution:
    def lastRemaining(self, n: int) -> int:
        if n <= 2:
            return n
        
        l, r, k = 1, n, 0
        while n > 1:
            if n&1 == 1:
                l = l + 2**k
                r = r - 2**k
            elif k&1 == 0:
                l = l + 2**k
            else:
                r = r - 2 ** k
            n //= 2
            k += 1
        return l
        