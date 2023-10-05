class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        
        res = 0
        p = 0
        x, y = 0, 0
        for i in range(n):
            if s[p] == s[i]:
                y += 1
            else:
                res += min(x, y)
                p = i
                x, y = y, 1
            
            if i == n-1:
                res += min(x, y)
        return res
