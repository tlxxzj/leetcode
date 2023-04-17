class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        ret = 0
        while len(g) > 0 and len(s) > 0:
            while len(s) > 0 and s[-1] < g[-1]:
                s.pop()
            if len(s) > 0 and s[-1] >= g[-1]:
                g.pop()
                s.pop()
                ret += 1
        return ret
