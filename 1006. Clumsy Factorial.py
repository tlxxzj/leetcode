class Solution:
    def clumsy(self, N: int) -> int:
        ret = 0
        f = 1
        while N >= 4:
            ret += f * (N*(N-1)//(N-2)) + N-3
            f = -1
            N -= 4
        if N == 3:
            ret += f * 3*2//1 
        if N == 2:
            ret += f * 2 * 1 
        if N == 1:
            ret += f * 1
        return ret
        