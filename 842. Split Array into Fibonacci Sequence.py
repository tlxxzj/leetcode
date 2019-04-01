class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        inf = (1<<31) - 1
        for i in range(1, n):
            for j in range(i+1, n):
                k = 0
                ret = []
                while 1:
                    a, b = S[k:i], S[i:j]
                    if (a.startswith('0') and len(a) > 1) or (b.startswith('0') and len(b) > 1) or len(a) == 0 or len(b) == 0:
                        break
                    x, y = int(a), int(b)
                    z = x+y
                    c = str(z)
                    if not S[j:].startswith(c):
                        break
                    if x >inf or y >inf or z >inf :
                        break
                    if k == 0:
                        ret = [x, y]
                    ret.append(z)
                    k, i, j = i, j, j+len(c)

                if j == n:
                    return ret
                    
        return []