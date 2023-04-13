class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = list(s), list(t)
        s.sort()
        t.sort()
        n = len(s)
        for i in range(n):
            if s[i] != t[i]:
                return t[i]
        return t[-1]