class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            return b if a%b == 0 else gcd(b, a%b)
        
        ret = []
        for i in range(1, n):
            for j in range(i+1, n+1):
                if gcd(i, j) == 1:
                    ret.append(f'{i}/{j}')
        return ret