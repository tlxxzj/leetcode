class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0] * 26
        b = [0] * 26
        orda = ord('a')
        for c in s:
            a[ord(c) - orda] += 1
        for c in t:
            b[ord(c) - orda] += 1
        return a == b