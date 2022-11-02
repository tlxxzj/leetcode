class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ''
        num = columnNumber
        while num > 0:
            num -= 1
            ret = chr(ord('A') + (num % 26)) + ret
            num //= 26
        return ret