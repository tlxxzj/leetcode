class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def c2i(c):
            return ord(c)-ord('a')
        
        m, n = len(s), len(p)
        count = [0] * 26
        for c in p:
            count[c2i(c)] += 1
        
        res = []
        l = 0
        for r in range(m):
            i = c2i(s[r])
            count[i] -= 1
            
            while count[i] < 0:
                count[c2i(s[l])] += 1
                l += 1
            
            if r-l+1 == n:
                res.append(l)
                count[c2i(s[l])] += 1
                l += 1
        return res
