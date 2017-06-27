class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        fp = {}
        for c in s:
            fp[c] = fp.get(c, 0) + 1
        def cmp(a, b):
            if fp[a] == fp[b]: return ord(a) - ord(b)
            else: return fp[b] - fp[a]
        s = list(s)
        s.sort(cmp=cmp)
        return ''.join(s)
        