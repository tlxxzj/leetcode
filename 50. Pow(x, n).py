class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1.0/self.myPow(x, -n)
        
        y = self.myPow(x, n>>1)
        if n&1 == 1:
            return x*y*y
        else:
            return y*y