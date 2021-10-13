class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        p2 = set()
        for i in range(32):
            num = 1 << i
            num = ''.join(sorted(list(str(num))))
            p2.add(num)
        return ''.join(sorted(list(str(n)))) in p2