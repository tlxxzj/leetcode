class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (not s) or (not s.strip()):
            return 0
        
        p = [0, len(s)]
        tok = [0]
        def next_token():
            while p[0] < p[1] and s[p[0]].isspace():
                p[0] += 1
            if p[0] >= p[1]:
                tok[0] =  ['eof']
            elif s[p[0]].isdigit():
                begin = p[0]
                while p[0] < p[1] and s[p[0]].isdigit():
                    p[0] += 1
                tok[0] =  ['int', int(s[begin:p[0]])]
            else:
                op = s[p[0]]
                p[0] += 1
                tok[0] = [op]
        

        def expr():
            pass
        
        def factor():
            next_token()
            t = tok[0]
            next_token()
            return t[1]
        
        def times():
            x = factor()
            t = tok[0]
            while t[0] in ['*', '/']:
                if t[0] == '*':
                    x = x * factor()
                else:
                    x = x / factor()
                t = tok[0]
            return x
        
        def plus():
            x = times()
            t = tok[0]
            while t[0] in ['+', '-']:
                if t[0] == '+':
                    x = x + times()
                else:
                    x = x - times()
                t = tok[0]
            return x
        
        return plus()
        
        
            
        