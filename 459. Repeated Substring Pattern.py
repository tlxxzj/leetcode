class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check(s, n, k):
            for i in xrange(k, n, k):
                if s[:k] != s[i:i+k]:
                    return False
            return True
        import math
        n = len(s)
        if n>1 and check(s, n, 1):
            return True
        vi = [True] * (n+1)
        for i in xrange(2, n/2+1):
            if vi[i]  and n%i == 0:
                if check(s, n, n/i):
                    return True
                else:
                    for j in xrange(i, n, i):
                        vi[j]=False
        return False
        