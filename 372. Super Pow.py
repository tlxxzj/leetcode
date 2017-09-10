class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        
        def fastpow(x, y):
            ret = 1
            while y:
                if y&1:
                    ret *= x
                    ret %= 1337
                x *= x
                x %= 1337
                y /= 2
            return ret
        
        x = 0
        for i in b:
            x = x * 10 + i
        
        return fastpow(a, x)
        
        
        