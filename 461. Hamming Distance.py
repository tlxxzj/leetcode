class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = 0
        z = x^y
        while z > 0:
            z = z & (z-1)
            diff += 1
        return diff