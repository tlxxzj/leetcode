class Solution:
    def romanToInt(self, s: str) -> int:
        ret = []
        for c in s:
            if c == 'I':
                ret.append(1)
            elif c == 'V':
                ret.append(5)
            elif c == 'X':
                ret.append(10)
            elif c == 'L':
                ret.append(50)
            elif c == 'C':
                ret.append(100)
            elif c == 'D':
                ret.append(500)
            else:
                ret.append(1000)
        for i in range(len(ret)-1):
            if ret[i] < ret[i+1]:
                ret[i] = -ret[i]
        return sum(ret)