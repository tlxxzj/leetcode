class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return ''.join(sorted(list(str(n)))) in set([''.join(sorted(list(str(1<<i)))) for i in range(32)])