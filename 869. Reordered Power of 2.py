class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        x = 1
        s = set()
        while x <= 1000000000:
            y = ''.join(sorted(list(str(x))))
            s.add(y)
            x *= 2
        return ''.join(sorted(list(str(N)))) in s