class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ret = 0
        l = [0]
        lf = 0
        t = 0
        f = False
        for c in input + '\n':
            if c == '\n':
                if t >= len(l) or t == 0:
                    if t == 0:
                        l[t] = lf
                    else:
                        l.append(l[t-1] + lf + 1)
                else:
                    l[t] = l[t-1] + lf + 1
                if f:
                    ret = max(ret, l[t])
                lf = 0
                t = 0
                f = False
            elif c == '\t':
                t += 1
            else:
                lf += 1
                if c == '.':
                    f = True
            
        
        return ret