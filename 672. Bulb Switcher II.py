class Solution:
    def flipLights(self, n: int, m: int) -> int:
        if n == 0 or m == 0: return 1
        if n == 1: return 2
        if n == 2:
            if m == 1: return 3
            else: return 4
        if m == 1:
            return 4
        if m == 2:
            return 7
        return 8