class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        a, b = numerator, denominator
        flag = ''
        if a * b < 0:
            flag = '-'
        a, b = abs(a), abs(b)
        c = a // b
        d = a % b
        if d == 0:
            return flag + str(c)
        x = str(c)
        y = ''
        ds = set()
        dl = []
        while d != 0:
            if d in ds:
                i = dl.index(d)
                ret = flag + x + '.' + y[:i] + '(' + y[i:] + ')'
                return ret
            dl.append(d)
            ds.add(d)
            a = d * 10
            c = a // b
            d = a % b
            y += str(c)
            if d == 0:
                return flag + x + '.' + y