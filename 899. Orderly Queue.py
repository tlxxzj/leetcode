class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K >= 2:
            return ''.join(sorted(list(S)))
        
        n = len(S)
        mc = min(list(S))
        i = 0
        j = 1
        while j < n:
            if S[j] != mc:
                j += 1
                continue
            k = 0
            while k < n and S[(i+k)%n] == S[(j+k)%n]:
                k += 1
            if S[(i+k)%n] > S[(j+k)%n]:
                i = j
            if k == 0:
                k = 1
            j += k
        return S[i:] + S[:i]
        