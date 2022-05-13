class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        a, b = x, 0
        while x > 0:
            b = (b * 10) + (x % 10)
            x //= 10
        return a == b