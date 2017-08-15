class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d, d2 = {}, {}
        for i in range(len(s)):
            a, b = s[i], t[i]
            if d.get(a, b) != b or d2.get(b,a)!=a:
                return False
            d[a] = b
            d2[b]=a
        return True
        