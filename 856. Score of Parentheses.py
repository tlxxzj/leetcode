class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ret = 0
        q = []
        for c in S:
            if c == '(':
                q.append(c)
            else:
                x = 0
                while q[-1] != '(':
                    x += q.pop()
                q.pop()
                y = max(2*x, 1)
                q.append(y)
        return sum(q)