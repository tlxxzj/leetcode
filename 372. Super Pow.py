class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        x = reduce(lambda x,y: x*10 + y, b, 0)
        
        def pow(k):
            if k == 0:
                return 1
            if k == 1:
                return a % 1337
            if k&1 == 1:
                y = pow(k//2)
                return y*y * a % 1337
            y = pow(k//2)
            return y*y % 1337
        
        return pow(x)