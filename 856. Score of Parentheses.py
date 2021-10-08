class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ret = []
        for c in s:
            if c == '(':
                ret.append(c)
            else:
                v = 0
                while ret[-1] != '(':
                    v += ret.pop()
                ret.pop()
                if v == 0:
                    ret.append(1)
                else:
                    ret.append(v*2)
        return sum(ret)