class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        for c in columnTitle:
            ret = ret * 26 + ord(c) - ord('A') + 1
        return ret