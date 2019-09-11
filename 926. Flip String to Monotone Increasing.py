class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        num0 = S.count('0')
        num1 = S.count('1')
        ret = min(num0, num1)
        n0, n1 = 0, 0
        for i in range(n):
            if S[i] == '0':
                n0 += 1
            else:
                n1 += 1
            ret = min(ret, n1 + num0 - n0)
        return ret
            