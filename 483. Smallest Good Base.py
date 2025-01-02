class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        n2 = n
        bits = 0
        while n2 > 0:
            n2 = n2 >> 1
            bits += 1
        
        while bits > 0:
            l, r = 2, n
            while l < r:
                m = (l + r) >> 1
                
                x = 1
                num = 1
                for i in range(bits):
                    x *= m
                    num += x
                    if num > n:
                        break

                if num < n:
                    l = m + 1
                elif num > n:
                    r = m
                else:
                    return str(m)
            bits -= 1
        
        return str(n-1)