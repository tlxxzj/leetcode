class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        a.reverse()
        b.reverse()
        c = [0]
        i = 0
        x = 0
        while i < len(a) or i < len(b) or x > 0:
            if i >= len(c):
                c.append(0)
            c[i] += x
            if i < len(a):
                c[i] += int(a[i])
            if i < len(b):
                c[i] += int(b[i])
            if c[i] > 1:
                x = c[i] // 2
                c[i] = c[i] % 2
            else:
                x = 0
            i += 1
        c.reverse()
        return ''.join(map(lambda x: str(x), c))