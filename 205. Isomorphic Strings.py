class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        m = {}
        m2 = {}
        for i in range(n):
            if s[i] in m:
                if m[s[i]] != t[i]:
                    return False
            if t[i] in m2:
                if m2[t[i]] != s[i]:
                    return False
            else:
                m[s[i]] = t[i]
                m2[t[i]] = s[i]
        return True
                