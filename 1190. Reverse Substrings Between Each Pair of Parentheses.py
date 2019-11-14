class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverse(S, l, r):
            while l < r:
                S[l], S[r] = S[r], S[l]
                l += 1
                r -= 1
        s = list(s)
        l, r = 0, len(s)-1
        p = []
        q = []
        for i in range(len(s)):
            if s[i] == '(':
                q.append(i)
            elif s[i] == ')':
                l, r = q.pop(), i
                s[l] = s[r] = ''
                p.append((l, r))
        for l, r in p:
            reverse(s, l, r)
        
        return ''.join(s)
        