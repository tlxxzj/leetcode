class Solution:
    def minSteps(self, n: int) -> int:
        ret = 0
        for i in range(2, n+1):
            while n % i == 0:
                ret += i
                n = n // i
        
        return ret