class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        n = len(s)
        n2 = (n << 1) | 1
        p = [1] * n2
        x = [1, 0]
        for c in s:
            x.append(c)
            x.append(0)
        x.append(2)
        i, id, mx, id2, mx2 = 1, 0, 0, 0, 0
        for i in range(1, n2):
            if mx > i:
                p[i] = min(p[2 * id - i],  mx - i)
            while x[i - p[i]] == x[i + p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                id = i
            if p[i] > mx2:
                mx2 = p[i]
                id2 = i
        ret = []
        for c in xrange(id2 - mx2 + 1, id2 + mx2):
            if x[c] != 0:
                ret.append(x[c])
        return ''.join(ret)


