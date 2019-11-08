class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l, r = 0, 0
        q = []
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                r += 1
            if r > l:
                r = l
                continue
            q.append(c)
        s = q
        s.reverse()
        q = []
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                r += 1
            if l > r:
                l = r
                continue
            q.append(c)
        q.reverse()
        return ''.join(q)