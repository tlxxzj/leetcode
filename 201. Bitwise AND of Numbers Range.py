class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ret = right
        x = right
        while x > 0:
            y = x & (-x)
            if left & y == 0 or right -y >= left:
                ret -= y
            x -= y
        return ret 