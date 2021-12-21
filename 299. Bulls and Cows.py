class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import defaultdict
        n = len(secret)
        a, b = 0, 0
        s, g = defaultdict(int), defaultdict(int)
        for i in range(n):
            if secret[i] == guess[i]:
                a += 1
            else:
                s[secret[i]] += 1
                g[guess[i]] += 1
        for key in g:
            if key in s:
                b += min(s[key], g[key])
        
        return f'{a}A{b}B'