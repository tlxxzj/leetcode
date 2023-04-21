class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = (l + r) // 2
            x = m * m
            if x < num:
                l = m + 1
            elif x > num:
                r = m - 1
            else:
                return True
        return False