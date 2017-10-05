class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (not needle):
            return 0
        if (not haystack):
            return -1
        
        def get_next(s):
            n = len(s)
            next = [-1] * (n + 1)
            i, j = -1, 0
            while j < n:
                if i == -1 or s[i] == s[j]:
                    i += 1
                    j += 1
                    next[j] = i
                else:
                    i = next[i]
            return next
        
        def kmp(s, p, next):
            sl, pl = len(s), len(p)
            i, j = 0, 0
            while i < sl and j < pl:
                if j == -1 or s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    j = next[j]
            if j == pl:
                return i - pl
            else:
                return -1
        
        return kmp(haystack, needle, get_next(needle))
        