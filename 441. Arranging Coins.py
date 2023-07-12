class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, 1<<31
        while l < r:
            m = (l + r) // 2
            if m*(m+1)//2 > n:
                r = m
            else:
                l = m + 1
        return r-1