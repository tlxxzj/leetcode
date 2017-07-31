class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ret = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            while j < len(s) and s[j]<g[i]:
                j += 1
            if j < len(s) and s[j] >= g[i]:
                ret += 1
                i += 1
                j += 1
        return ret
        